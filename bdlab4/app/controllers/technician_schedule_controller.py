from flask import Blueprint, request, jsonify
from ..dao.technician_schedule_dao import TechnicianScheduleDAO

technician_schedule_bp = Blueprint('technician_schedule', __name__)

@technician_schedule_bp.route('/technician_schedules', methods=['GET'])
def get_all_schedules():
    schedules = TechnicianScheduleDAO.get_all_schedules()
    return jsonify([schedule.to_dict() for schedule in schedules]), 200

@technician_schedule_bp.route('/technician_schedules/<int:schedule_id>', methods=['GET'])
def get_schedule(schedule_id):
    schedule = TechnicianScheduleDAO.get_schedule(schedule_id)
    if schedule is None:
        return jsonify({"message": "Schedule not found"}), 404
    return jsonify(schedule.to_dict()), 200

@technician_schedule_bp.route('/technician_schedules', methods=['POST'])
def create_schedule():
    data = request.json
    schedule = TechnicianScheduleDAO.create_schedule(data)
    return jsonify(schedule.to_dict()), 201

@technician_schedule_bp.route('/technician_schedules/<int:schedule_id>', methods=['PATCH'])
def update_schedule(schedule_id):
    data = request.json
    schedule = TechnicianScheduleDAO.update_schedule(schedule_id, data)
    if schedule is None:
        return jsonify({"message": "Schedule not found"}), 404
    return jsonify(schedule.to_dict()), 200

@technician_schedule_bp.route('/technician_schedules/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    TechnicianScheduleDAO.delete_schedule(schedule_id)
    return jsonify({"message": "Schedule deleted"}), 204
