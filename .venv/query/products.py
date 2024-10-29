from dataclasses import dataclass
from typing import List, Union


@dataclass
class ProductsResponse:
    data: List[str]
    status: bool
    error_message: str

def get_all_products(db_config):
    response = ProductsResponse(
        data=['1', '2', '3'],
        status=True,
        error_message=''
    )
    return response