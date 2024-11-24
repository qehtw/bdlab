# app/controllers/manufacturer_controller.py
from flask import Blueprint, request, jsonify
from ..dao.manufacturer_dao import ManufacturerDAO

manufacturer_bp = Blueprint('manufacturer', __name__)

@manufacturer_bp.route('/manufacturers', methods=['GET'])
def get_all_manufacturers():
    manufacturers = ManufacturerDAO.get_all_manufacturers()
    return jsonify([manufacturer.to_dict() for manufacturer in manufacturers]), 200

@manufacturer_bp.route('/manufacturers/<int:manufacturer_id>', methods=['GET'])
def get_manufacturer(manufacturer_id):
    manufacturer = ManufacturerDAO.get_manufacturer(manufacturer_id)
    if manufacturer is None:
        return jsonify({"message": "Manufacturer not found"}), 404
    return jsonify(manufacturer.to_dict()), 200

@manufacturer_bp.route('/manufacturers', methods=['POST'])
def create_manufacturer():
    data = request.json
    manufacturer = ManufacturerDAO.create_manufacturer(data)
    return jsonify(manufacturer.to_dict()), 201

@manufacturer_bp.route('/manufacturers/<int:manufacturer_id>', methods=['PATCH'])
def update_manufacturer(manufacturer_id):
    data = request.json
    manufacturer = ManufacturerDAO.update_manufacturer(manufacturer_id, data)
    return jsonify(manufacturer.to_dict()), 200

@manufacturer_bp.route('/manufacturers/<int:manufacturer_id>', methods=['DELETE'])
def delete_manufacturer(manufacturer_id):
    ManufacturerDAO.delete_manufacturer(manufacturer_id)
    return jsonify({"message": "Manufacturer deleted"}), 204
