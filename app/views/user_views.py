from flask import Blueprint, render_template
from app.models import User

user_views_bp = Blueprint('user_views', __name__)

@user_views_bp.route('/users')
def user_list():
    # Retrieve a list of users and render the user list template
    users = User.query.all()
    return render_template('user_list.html', users=users)

@user_views_bp.route('/user/<int:user_id>')
def user_detail(user_id):
    # Retrieve a user by ID and render the user detail template
   user = User.query.get(user_id)
    if user:
        return render_template('user_detail.html', user=user)
    return 'User not found', 404
