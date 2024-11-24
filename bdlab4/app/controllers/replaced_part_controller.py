# app/controllers/replaced_part_controller.py
from flask import Blueprint, request, jsonify
from ..dao.replaced_part_dao import ReplacedPartDAO

replaced_part_bp = Blueprint('replaced_part', __name__)

@replaced_part_bp.route('/replaced_parts', methods=['GET'])
def get_all_replaced_parts():
    replaced_parts = ReplacedPartDAO.get_all_replaced_parts()
    return jsonify([rp.to_dict() for rp in replaced_parts]), 200

@replaced_part_bp.route('/replaced_parts/<int:replaced_part_id>', methods=['GET'])
def get_replaced_part(replaced_part_id):
    replaced_part = ReplacedPartDAO.get_replaced_part(replaced_part_id)
    if replaced_part is None:
        return jsonify({"message": "Replaced part not found"}), 404
    return jsonify(replaced_part.to_dict()), 200

@replaced_part_bp.route('/replaced_parts', methods=['POST'])
def create_replaced_part():
    data = request.json
    replaced_part = ReplacedPartDAO.create_replaced_part(data)
    return jsonify(replaced_part.to_dict()), 201

@replaced_part_bp.route('/replaced_parts/<int:replaced_part_id>', methods=['PATCH'])
def update_replaced_part(replaced_part_id):
    data = request.json
    replaced_part = ReplacedPartDAO.update_replaced_part(replaced_part_id, data)
    return jsonify(replaced_part.to_dict()), 200

@replaced_part_bp.route('/replaced_parts/<int:replaced_part_id>', methods=['DELETE'])
def delete_replaced_part(replaced_part_id):
    ReplacedPartDAO.delete_replaced_part(replaced_part_id)
    return jsonify({"message": "Replaced part deleted"}), 204
