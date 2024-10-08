from flask import Blueprint, request, jsonify
from app.models import User

users_api_bp = Blueprint('users_api', __name__)

@users_api_bp.route('/', methods=['GET'])
def get_users():
    # Retrieve a list of users
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@users_api_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Retrieve a user by ID
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'message': 'User not found'}), 404
