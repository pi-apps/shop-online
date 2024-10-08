from flask import Blueprint, request, jsonify
from app.models import Order

orders_api_bp = Blueprint('orders_api', __name__)

@orders_api_bp.route('/', methods=['GET'])
def get_orders():
    # Retrieve a list of orders
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders])

@orders_api_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # Retrieve an order by ID
    order = Order.query.get(order_id)
    if order:
        return jsonify(order.to_dict())
    return jsonify({'message': 'Order not found'}), 404
