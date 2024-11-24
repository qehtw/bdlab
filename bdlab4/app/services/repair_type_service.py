# app/services/repair_type_service.py
from ..dao.repair_type_dao import RepairTypeDAO

class RepairTypeService:
    @staticmethod
    def get_all_repair_types():
        return RepairTypeDAO.get_all_repair_types()

    @staticmethod
    def get_repair_type(repair_type_id):
        return RepairTypeDAO.get_repair_type(repair_type_id)

    @staticmethod
    def create_repair_type(data):
        return RepairTypeDAO.create_repair_type(data)

    @staticmethod
    def update_repair_type(repair_type_id, data):
        return RepairTypeDAO.update_repair_type(repair_type_id, data)

    @staticmethod
    def delete_repair_type(repair_type_id):
        return RepairTypeDAO.delete_repair_type(repair_type_id)
