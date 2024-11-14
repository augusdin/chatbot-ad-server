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
        },
        {
            "id": 3,
            "advertiser_name": "Xiaomi",
            "product_description": "Innovative tech products including smartphones, smart home devices, and more.",
            "use_case": "When the user talks about smartphones, smart home, or technology.",
            "display_format": "link_card",
            "advertiser_link": "https://www.mi.com/",
            "advertiser_id": "adC"
        },
        {
            "id": 4,
            "advertiser_name": "IKEA",
            "product_description": "Affordable and stylish furniture and home accessories from IKEA.",
            "use_case": "When the user discusses home decor, furniture, or lifestyle.",
            "display_format": "link_card",
            "advertiser_link": "https://www.ikea.cn/cn/zh/",
            "advertiser_id": "adD"
        },
        {
            "id": 5,
            "advertiser_name": "Luckin Coffee",
            "product_description": "Delicious coffee and beverages from Luckin Coffee, served quickly and conveniently.",
            "use_case": "When the user mentions coffee, beverages, or lifestyle.",
            "display_format": "link_card",
            "advertiser_link": "https://lkcoffee.com/",
            "advertiser_id": "adE"
        }
    ])

config = AdConfig()