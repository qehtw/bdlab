# app/controllers/repair_type_controller.py
from flask import Blueprint, request, jsonify
from ..dao.repair_type_dao import RepairTypeDAO

repair_type_bp = Blueprint('repair_type', __name__)

@repair_type_bp.route('/repair_types', methods=['GET'])
def get_all_repair_types():
    repair_types = RepairTypeDAO.get_all_repair_types()
    return jsonify([repair_type.to_dict() for repair_type in repair_types]), 200

@repair_type_bp.route('/repair_types/<int:repair_type_id>', methods=['GET'])
def get_repair_type(repair_type_id):
    repair_type = RepairTypeDAO.get_repair_type(repair_type_id)
    if repair_type is None:
        return jsonify({"message": "Repair type not found"}), 404
    return jsonify(repair_type.to_dict()), 200

@repair_type_bp.route('/repair_types', methods=['POST'])
def create_repair_type():
    data = request.json
    repair_type = RepairTypeDAO.create_repair_type(data)
    return jsonify(repair_type.to_dict()), 201

@repair_type_bp.route('/repair_types/<int:repair_type_id>', methods=['PATCH'])
def update_repair_type(repair_type_id):
    data = request.json
    repair_type = RepairTypeDAO.update_repair_type(repair_type_id, data)
    return jsonify(repair_type.to_dict()), 200

@repair_type_bp.route('/repair_types/<int:repair_type_id>', methods=['DELETE'])
def delete_repair_type(repair_type_id):
    RepairTypeDAO.delete_repair_type(repair_type_id)
    return jsonify({"message": "Repair type deleted"}), 204
