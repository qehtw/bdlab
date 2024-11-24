# app/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from ..dao.user_dao import UserDAO

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = UserDAO.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserDAO.get_user(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user.to_dict()), 200

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = UserDAO.create_user(data)
    return jsonify(user.to_dict()), 201

@user_bp.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.json
    user = UserDAO.update_user(user_id, data)
    return jsonify(user.to_dict()), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserDAO.delete_user(user_id)
    return jsonify({"message": "User deleted"}), 204
