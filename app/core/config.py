from pydantic import BaseModel, Field
from typing import List, Dict, Union

class AdConfig(BaseModel):
    ads: List[Dict[str, Union[str, int]]] = Field(default_factory=lambda: [
        {
            "id": 1,
            "advertiser_name": "Apple",
            "product_description": "Latest Apple products including iPhones, Macs, and more.",
            "use_case": "When the user talks about Apple or technology.",
            "display_format": "link_card",
            "advertiser_link": "https://www.apple.com.cn/",
            "advertiser_id": "adA"
        },
        {
            "id": 2,
            "advertiser_name": "Li-Ning",
            "product_description": "High-quality sportswear and equipment from Li-Ning.",
            "use_case": "When the user discusses sports or entertainment.",
            "display_format": "link_card",
            "advertiser_link": "https://www.lining.com/",
            "advertiser_id": "adB"
        }
    ])

config = AdConfig()