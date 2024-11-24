from flask import Blueprint, request, jsonify
from ..dao.technician_repairs_dao import TechnicianRepairsDAO

technician_repairs_bp = Blueprint('technician_repairs', __name__)

@technician_repairs_bp.route('/technician_repairs', methods=['GET'])
def get_all_technician_repairs():
    repairs = TechnicianRepairsDAO.get_all_technician_repairs()
    return jsonify([{
        "technician_id": repair.technician_id,
        "repair_id": repair.repair_id,
        "technician": repair.technician.to_dict() if repair.technician else None,
        "repair": repair.repair.to_dict() if repair.repair else None
    } for repair in repairs]), 200

@technician_repairs_bp.route('/technician_repairs/<int:technician_id>/<int:repair_id>', methods=['GET'])
def get_technician_repair(technician_id, repair_id):
    repair = TechnicianRepairsDAO.get_technician_repair(technician_id, repair_id)
    if repair is None:
        return jsonify({"message": "Technician repair not found"}), 404
    return jsonify({
        "technician_id": repair.technician_id,
        "repair_id": repair.repair_id,
        "technician": repair.technician.to_dict() if repair.technician else None,
        "repair": repair.repair.to_dict() if repair.repair else None
    }), 200

@technician_repairs_bp.route('/technician_repairs/technician/<int:technician_id>', methods=['GET'])
def get_repairs_for_technician(technician_id):
    repairs = TechnicianRepairsDAO.get_repairs_by_technician(technician_id)
    if not repairs:
        return jsonify({"message": "No repairs found for this technician"}), 404
    return jsonify([{
        "technician_id": repair.technician_id,
        "repair_id": repair.repair_id,
        "technician": repair.technician.to_dict() if repair.technician else None,
        "repair": repair.repair.to_dict() if repair.repair else None
    } for repair in repairs]), 200

@technician_repairs_bp.route('/technician_repairs', methods=['POST'])
def create_technician_repair():
    data = request.json
    repair = TechnicianRepairsDAO.create_technician_repair(data)
    return jsonify({
        "technician_id": repair.technician_id,
        "repair_id": repair.repair_id,
        "technician": repair.technician.to_dict() if repair.technician else None,
        "repair": repair.repair.to_dict() if repair.repair else None
    }), 201

@technician_repairs_bp.route('/technician_repairs/<int:technician_id>/<int:repair_id>', methods=['PATCH'])
def update_technician_repair(technician_id, repair_id):
    data = request.json
    repair = TechnicianRepairsDAO.update_technician_repair(technician_id, repair_id, data)
    return jsonify({
        "technician_id": repair.technician_id,
        "repair_id": repair.repair_id,
        "technician": repair.technician.to_dict() if repair.technician else None,
        "repair": repair.repair.to_dict() if repair.repair else None
    }), 200

@technician_repairs_bp.route('/technician_repairs/<int:technician_id>/<int:repair_id>', methods=['DELETE'])
def delete_technician_repair(technician_id, repair_id):
    TechnicianRepairsDAO.delete_technician_repair(technician_id, repair_id)
    return jsonify({"message": "Technician repair deleted"}), 204
