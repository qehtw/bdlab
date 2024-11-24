# app/services/spare_part_service.py
from ..dao.spare_part_dao import SparePartDAO

class SparePartService:
    @staticmethod
    def get_all_spare_parts():
        return SparePartDAO.get_all_spare_parts()

    @staticmethod
    def get_spare_part(spare_part_id):
        return SparePartDAO.get_spare_part(spare_part_id)

    @staticmethod
    def create_spare_part(data):
        return SparePartDAO.create_spare_part(data)

    @staticmethod
    def update_spare_part(spare_part_id, data):
        return SparePartDAO.update_spare_part(spare_part_id, data)

    @staticmethod
    def delete_spare_part(spare_part_id):
        return SparePartDAO.delete_spare_part(spare_part_id)
