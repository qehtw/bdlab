# app/services/equipment_service.py
from ..dao.equipment_dao import EquipmentDAO

class EquipmentService:
    @staticmethod
    def get_all_equipments():
        return EquipmentDAO.get_all_equipments()

    @staticmethod
    def get_equipment(equipment_id):
        return EquipmentDAO.get_equipment(equipment_id)

    @staticmethod
    def create_equipment(data):
        return EquipmentDAO.create_equipment(data)

    @staticmethod
    def update_equipment(equipment_id, data):
        return EquipmentDAO.update_equipment(equipment_id, data)

    @staticmethod
    def delete_equipment(equipment_id):
        return EquipmentDAO.delete_equipment(equipment_id)
