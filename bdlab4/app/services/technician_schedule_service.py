# app/services/technician_schedule_service.py
from ..dao.technician_schedule_dao import TechnicianScheduleDAO

class TechnicianScheduleService:
    @staticmethod
    def get_all_schedules():
        return TechnicianScheduleDAO.get_all_schedules()

    @staticmethod
    def get_schedule(schedule_id):
        return TechnicianScheduleDAO.get_schedule(schedule_id)

    @staticmethod
    def create_schedule(data):
        return TechnicianScheduleDAO.create_schedule(data)

    @staticmethod
    def update_schedule(schedule_id, data):
        return TechnicianScheduleDAO.update_schedule(schedule_id, data)

    @staticmethod
    def delete_schedule(schedule_id):
        return TechnicianScheduleDAO.delete_schedule(schedule_id)
