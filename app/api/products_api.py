from flask import Blueprint, request, jsonify
from app.models import Product

products_api_bp = Blueprint('products_api', __name__)

@products_api_bp.route('/', methods=['GET'])
def get_products():
    # Retrieve a list of products
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@products_api_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Retrieve a product by ID
    product = Product.query.get(product_id)
    if product:
        return jsonify(product.to_dict())
    return jsonify({'message': 'Product not found'}), 404
