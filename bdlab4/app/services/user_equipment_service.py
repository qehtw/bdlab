# app/services/user_equipment_service.py
from ..dao.user_equipment_dao import UserEquipmentDAO

class UserEquipmentService:
    @staticmethod
    def get_all_user_equipment():
        return UserEquipmentDAO.get_all_user_equipment()

    @staticmethod
    def get_user_equipment(user_equipment_id):
        return UserEquipmentDAO.get_user_equipment(user_equipment_id)

    @staticmethod
    def create_user_equipment(data):
        return UserEquipmentDAO.create_user_equipment(data)

    @staticmethod
    def update_user_equipment(user_equipment_id, data):
        return UserEquipmentDAO.update_user_equipment(user_equipment_id, data)

    @staticmethod
    def delete_user_equipment(user_equipment_id):
        return UserEquipmentDAO.delete_user_equipment(user_equipment_id)
