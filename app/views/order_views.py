from flask import Blueprint, render_template
from app.models import Order

order_views_bp = Blueprint('order_views', __name__)

@order_views_bp.route('/orders')
def order_list():
    # Retrieve a list of orders and render the order list template
    orders = Order.query.all()
    return render_template('order_list.html', orders=orders)

@order_views_bp.route('/order/<int:order_id>')
def order_detail(order_id):
    # Retrieve an order by ID and render the order detail template
    order = Order.query.get(order_id)
    if order:
        return render_template('order_detail.html', order=order)
    return 'Order not found', 404
