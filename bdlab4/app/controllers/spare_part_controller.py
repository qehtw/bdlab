# app/controllers/spare_part_controller.py
from flask import Blueprint, request, jsonify
from ..dao.spare_part_dao import SparePartDAO

spare_part_bp = Blueprint('spare_part', __name__)

@spare_part_bp.route('/spare_parts', methods=['GET'])
def get_all_spare_parts():
    spare_parts = SparePartDAO.get_all_spare_parts()
    return jsonify([part.to_dict() for part in spare_parts]), 200

@spare_part_bp.route('/spare_parts/<int:part_id>', methods=['GET'])
def get_spare_part(part_id):
    part = SparePartDAO.get_spare_part(part_id)
    if part is None:
        return jsonify({"message": "Spare part not found"}), 404
    return jsonify(part.to_dict()), 200

@spare_part_bp.route('/spare_parts', methods=['POST'])
def create_spare_part():
    data = request.json
    part = SparePartDAO.create_spare_part(data)
    return jsonify(part.to_dict()), 201

@spare_part_bp.route('/spare_parts/<int:part_id>', methods=['PATCH'])
def update_spare_part(part_id):
    data = request.json
    part = SparePartDAO.update_spare_part(part_id, data)
    return jsonify(part.to_dict()), 200

@spare_part_bp.route('/spare_parts/<int:part_id>', methods=['DELETE'])
def delete_spare_part(part_id):
    SparePartDAO.delete_spare_part(part_id)
    return jsonify({"message": "Spare part deleted"}), 204
