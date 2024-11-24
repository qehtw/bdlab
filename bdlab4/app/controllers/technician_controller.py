# app/controllers/technician_controller.py
from flask import Blueprint, request, jsonify
from ..dao.technician_dao import TechnicianDAO

technician_bp = Blueprint('technician', __name__)

@technician_bp.route('/technicians', methods=['GET'])
def get_all_technicians():
    technicians = TechnicianDAO.get_all_technicians()
    return jsonify([tech.to_dict() for tech in technicians]), 200

@technician_bp.route('/technicians/<int:technician_id>', methods=['GET'])
def get_technician(technician_id):
    technician = TechnicianDAO.get_technician(technician_id)
    if technician is None:
        return jsonify({"message": "Technician not found"}), 404
    return jsonify(technician.to_dict()), 200

@technician_bp.route('/technicians', methods=['POST'])
def create_technician():
    data = request.json
    technician = TechnicianDAO.create_technician(data)
    return jsonify(technician.to_dict()), 201

@technician_bp.route('/technicians/<int:technician_id>', methods=['PATCH'])
def update_technician(technician_id):
    data = request.json
    technician = TechnicianDAO.update_technician(technician_id, data)
    return jsonify(technician.to_dict()), 200

@technician_bp.route('/technicians/<int:technician_id>', methods=['DELETE'])
def delete_technician(technician_id):
    TechnicianDAO.delete_technician(technician_id)
    return jsonify({"message": "Technician deleted"}), 204
