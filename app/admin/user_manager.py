from flask import Blueprint, request, jsonify
from app.models import User

user_manager_bp = Blueprint('user_manager', __name__)

@user_manager_bp.route('/create', methods=['POST'])
def create_user():
    # Create a new user
    user_data = request.get_json()
    user = User(**user_data)
    user.save()
    return jsonify({'message': 'User created successfully'})

@user_manager_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Retrieve a user by ID
    user = User.query.get(user_id)
    if user:
        return jsonify({'user': user.to_dict()})
    return jsonify({'message': 'User not found'}), 404

@user_manager_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Update a user
    user_data = request.get_json()
    user = User.query.get(user_id)
    if user:
        user.update(**user_data)
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404

@user_manager_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Delete a user
    user = User.query.get(user_id)
    if user:
        user.delete()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404
