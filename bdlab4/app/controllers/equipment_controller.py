# app/controllers/equipment_controller.py
from flask import Blueprint, request, jsonify
from ..dao.equipment_dao import EquipmentDAO

equipment_bp = Blueprint('equipment', __name__)

@equipment_bp.route('/equipment', methods=['GET'])
def get_all_equipment():
    equipment = EquipmentDAO.get_all_equipments()
    return jsonify([eq.to_dict() for eq in equipment]), 200

@equipment_bp.route('/equipment/<int:equipment_id>', methods=['GET'])
def get_equipment(equipment_id):
    equipment = EquipmentDAO.get_equipment(equipment_id)
    if equipment is None:
        return jsonify({"message": "Equipment not found"}), 404
    return jsonify(equipment.to_dict()), 200

@equipment_bp.route('/equipment', methods=['POST'])
def create_equipment():
    data = request.json
    equipment = EquipmentDAO.create_equipment(data)
    return jsonify(equipment.to_dict()), 201

@equipment_bp.route('/equipment/<int:equipment_id>', methods=['PATCH'])
def update_equipment(equipment_id):
    data = request.json
    equipment = EquipmentDAO.update_equipment(equipment_id, data)
    return jsonify(equipment.to_dict()), 200

@equipment_bp.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    EquipmentDAO.delete_equipment(equipment_id)
    return jsonify({"message": "Equipment deleted"}), 204
