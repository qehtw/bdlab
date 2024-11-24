# app/services/repair_service.py
from ..dao.repair_dao import RepairDAO

class RepairService:
    @staticmethod
    def get_all_repairs():
        return RepairDAO.get_all_repairs()

    @staticmethod
    def get_repair(repair_id):
        return RepairDAO.get_repair(repair_id)

    @staticmethod
    def create_repair(data):
        return RepairDAO.create_repair(data)

    @staticmethod
    def update_repair(repair_id, data):
        return RepairDAO.update_repair(repair_id, data)

    @staticmethod
    def delete_repair(repair_id):
        return RepairDAO.delete_repair(repair_id)
