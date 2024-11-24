# app/controllers/user_equipment_controller.py
from flask import Blueprint, request, jsonify
from ..dao.user_equipment_dao import UserEquipmentDAO

user_equipment_bp = Blueprint('user_equipment', __name__)

@user_equipment_bp.route('/user_equipment', methods=['GET'])
def get_all_user_equipment():
    user_equipment = UserEquipmentDAO.get_all_user_equipment()
    return jsonify([ue.to_dict() for ue in user_equipment]), 200

@user_equipment_bp.route('/user_equipment/<int:user_equipment_id>', methods=['GET'])
def get_user_equipment(user_equipment_id):
    user_equipment = UserEquipmentDAO.get_user_equipment(user_equipment_id)
    if user_equipment is None:
        return jsonify({"message": "User equipment not found"}), 404
    return jsonify(user_equipment.to_dict()), 200

@user_equipment_bp.route('/user_equipment', methods=['POST'])
def create_user_equipment():
    data = request.json
    user_equipment = UserEquipmentDAO.create_user_equipment(data)
    return jsonify(user_equipment.to_dict()), 201

@user_equipment_bp.route('/user_equipment/<int:user_equipment_id>', methods=['PATCH'])
def update_user_equipment(user_equipment_id):
    data = request.json
    user_equipment = UserEquipmentDAO.update_user_equipment(user_equipment_id, data)
    return jsonify(user_equipment.to_dict()), 200

@user_equipment_bp.route('/user_equipment/<int:user_equipment_id>', methods=['DELETE'])
def delete_user_equipment(user_equipment_id):
    UserEquipmentDAO.delete_user_equipment(user_equipment_id)
    return jsonify({"message": "User equipment deleted"}), 204
