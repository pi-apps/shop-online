from flask import Blueprint, request, jsonify
from app.models import Product

product_manager_bp = Blueprint('product_manager', __name__)

@product_manager_bp.route('/create', methods=['POST'])
def create_product():
    # Create a new product
    product_data = request.get_json()
    product = Product(**product_data)
    product.save()
    return jsonify({'message': 'Product created successfully'})

@product_manager_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Retrieve a product by ID
    product = Product.query.get(product_id)
    if product:
        return jsonify({'product': product.to_dict()})
    return jsonify({'message': 'Product not found'}), 404

@product_manager_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Update a product
    product_data = request.get_json()
    product = Product.query.get(product_id)
    if product:
        product.update(**product_data)
        return jsonify({'message': 'Product updated successfully'})
    return jsonify({'message': 'Product not found'}), 404

@product_manager_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Delete a product
    product = Product.query.get(product_id)
    if product:
        product.delete()
        return jsonify({'message': 'Product deleted successfully'})
    return jsonify({'message': 'Product not found'}), 404
