from flask import Blueprint, render_template
from products import ProductsResponse, get_all_products

query_blueprint = Blueprint(
    'query_bp',
    __name__,
)

@query_blueprint.route('/', methods = ['GET'])
def get_all_products_handler() -> str:
    #  ... db_execute
    response: ProductsResponse = get_all_products(db_config=...)
    return render_template('...', content=response)

@query_blueprint.route('/', methods = ['POST'])
def get_product_handler(): pass