# app/services/replaced_part_service.py
from ..dao.replaced_part_dao import ReplacedPartDAO

class ReplacedPartService:
    @staticmethod
    def get_all_replaced_parts():
        return ReplacedPartDAO.get_all_replaced_parts()

    @staticmethod
    def get_replaced_part(replaced_part_id):
        return ReplacedPartDAO.get_replaced_part(replaced_part_id)

    @staticmethod
    def create_replaced_part(data):
        return ReplacedPartDAO.create_replaced_part(data)

    @staticmethod
    def update_replaced_part(replaced_part_id, data):
        return ReplacedPartDAO.update_replaced_part(replaced_part_id, data)

    @staticmethod
    def delete_replaced_part(replaced_part_id):
        return ReplacedPartDAO.delete_replaced_part(replaced_part_id)
