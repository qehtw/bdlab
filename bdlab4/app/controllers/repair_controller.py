# app/controllers/repair_controller.py
from flask import Blueprint, request, jsonify
from ..dao.repair_dao import RepairDAO

repair_bp = Blueprint('repair', __name__)

@repair_bp.route('/repairs', methods=['GET'])
def get_all_repairs():
    repairs = RepairDAO.get_all_repairs()
    return jsonify([repair.to_dict() for repair in repairs]), 200

@repair_bp.route('/repairs/<int:repair_id>', methods=['GET'])
def get_repair(repair_id):
    repair = RepairDAO.get_repair(repair_id)
    if repair is None:
        return jsonify({"message": "Repair not found"}), 404
    return jsonify(repair.to_dict()), 200

@repair_bp.route('/repairs', methods=['POST'])
def create_repair():
    data = request.json
    repair = RepairDAO.create_repair(data)
    return jsonify(repair.to_dict()), 201

@repair_bp.route('/repairs/<int:repair_id>', methods=['PATCH'])
def update_repair(repair_id):
    data = request.json
    repair = RepairDAO.update_repair(repair_id, data)
    return jsonify(repair.to_dict()), 200

@repair_bp.route('/repairs/<int:repair_id>', methods=['DELETE'])
def delete_repair(repair_id):
    RepairDAO.delete_repair(repair_id)
    return jsonify({"message": "Repair deleted"}), 204
