from flask import Blueprint, request, jsonify
from app.models import Order

order_manager_bp = Blueprint('order_manager', __name__)

@order_manager_bp.route('/create', methods=['POST'])
def create_order():
    # Create a new order
    order_data = request.get_json()
    order = Order(**order_data)
    order.save()
    return jsonify({'message': 'Order created successfully'})

@order_manager_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # Retrieve an order by ID
    order = Order.query.get(order_id)
    if order:
        return jsonify({'order': order.to_dict()})
    return jsonify({'message': 'Order not found'}), 404

@order_manager_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    # Update an order
    order_data = request.get_json()
    order = Order.query.get(order_id)
    if order:
        order.update(**order_data)
        return jsonify({'message': 'Order updated successfully'})
    return jsonify({'message': 'Order not found'}), 404

@order_manager_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    # Delete an order
    order = Order.query.get(order_id)
    if order:
        order.delete()
        return jsonify({'message': 'Order deleted successfully'})
    return jsonify({'message': 'Order not found'}), 404
