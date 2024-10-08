from flask import Blueprint, render_template
from app.models import Product

product_views_bp = Blueprint('product_views', __name__)

@product_views_bp.route('/products')
def product_list():
    # Retrieve a list of products and render the product list template
    products = Product.query.all()
    return render_template('product_list.html', products=products)

@product_views_bp.route('/product/<int:product_id>')
def product_detail(product_id):
    # Retrieve a product by ID and render the product detail template
    product = Product.query.get(product_id)
    if product:
        return render_template('product_detail.html', product=product)
    return 'Product not found', 404
