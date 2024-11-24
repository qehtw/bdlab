# app/services/technician_service.py
from ..dao.technician_dao import TechnicianDAO

class TechnicianService:
    @staticmethod
    def get_all_technicians():
        return TechnicianDAO.get_all_technicians()

    @staticmethod
    def get_technician(technician_id):
        return TechnicianDAO.get_technician(technician_id)

    @staticmethod
    def create_technician(data):
        return TechnicianDAO.create_technician(data)

    @staticmethod
    def update_technician(technician_id, data):
        return TechnicianDAO.update_technician(technician_id, data)

    @staticmethod
    def delete_technician(technician_id):
        return TechnicianDAO.delete_technician(technician_id)
