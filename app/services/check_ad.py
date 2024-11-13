# app/services/check_ad.py

import os
import json
from openai import OpenAI
from typing import List, Dict, Union, Optional
from app.core.config import config
from fastapi import HTTPException

API_KEY = 'sk-fGpATxGXaxUL9EcaB2Fa9580662841De9bB2E9FfB5323dCc'
if not API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

BASE_URL = "https://aihubmix.com/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

class AdMatchingError(Exception):
    """Custom exception for ad matching errors"""
    def __init__(self, message: str, details: Optional[Dict] = None):
        self.message = message
        self.details = details
        super().__init__(self.message)

def generate_prompt(messages: List[Dict[str, str]]) -> str:
    conversation = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
    ad_descriptions = "\n".join([
        f"Ad {ad['id']}:\n"
        f"Advertiser Name: {ad['advertiser_name']}\n"
        f"Product Description: {ad['product_description']}\n"
        f"Use Case: {ad['use_case']}\n"
        for ad in config.ads
    ])

    return (
        f"Here is a conversation between a user and an assistant:\n\n{conversation}\n\n"
        f"The following are ads and their details:\n{ad_descriptions}\n"
        "Please determine if any of the ads are relevant to the conversation. "
        "Respond in JSON format. If any ad is relevant, respond with "
        '{"isMatched": true, "matchedAdId": <ad_id>}. '
        "If no ads match, respond with {\"isMatched\": false}."
    )

def check_advertisement(messages: List[Dict[str, str]]) -> Dict[str, Union[str, bool, None]]:
    try:
        prompt = generate_prompt(messages)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that matches ads to conversations."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.3
        )

        if not response.choices or not response.choices[0].message.content:
            raise AdMatchingError("Empty response from OpenAI API")

        result = response.choices[0].message.content.strip()
        print("OpenAI API response:", result)  # 调试日志

        try:
            match_data = json.loads(result)
        except json.JSONDecodeError as e:
            raise AdMatchingError(
                "Failed to parse API response",
                {"raw_response": result, "error": str(e)}
            )

        if not isinstance(match_data, dict):
            raise AdMatchingError(
                "Invalid response format",
                {"raw_response": result}
            )

        if match_data.get("isMatched") and "matchedAdId" in match_data:
            matched_ad_id = match_data["matchedAdId"]
            matched_ad = next((ad for ad in config.ads if ad["id"] == matched_ad_id), None)
            
            if not matched_ad:
                raise AdMatchingError(
                    f"Matched ad ID {matched_ad_id} not found in config",
                    {"matched_id": matched_ad_id}
                )

            return {
                "show_ad": True,
                "advertiser_name": str(matched_ad["advertiser_name"]),
                "ad_use_case": str(matched_ad["use_case"]),
                "display_format": str(matched_ad["display_format"]),
                "advertiser_link": str(matched_ad["advertiser_link"])
            }

        return {
            "show_ad": False,
            "advertiser_name": None,
            "ad_use_case": None,
            "display_format": None,
            "advertiser_link": None
        }

    except AdMatchingError as e:
        error_msg = f"Ad matching error: {e.message}"
        print(f"{error_msg} - Details: {e.details}")  # 调试日志
        raise HTTPException(
            status_code=500,
            detail={
                "error": "ad_matching_error",
                "message": e.message,
                "details": e.details
            }
        )
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(error_msg)  # 调试日志
        raise HTTPException(
            status_code=500,
            detail={
                "error": "internal_server_error",
                "message": "An unexpected error occurred during ad matching",
                "details": str(e)
            }
        )