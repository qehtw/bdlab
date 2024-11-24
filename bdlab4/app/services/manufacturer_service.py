# app/services/manufacturer_service.py
from ..dao.manufacturer_dao import ManufacturerDAO

class ManufacturerService:
    @staticmethod
    def get_all_manufacturers():
        return ManufacturerDAO.get_all_manufacturers()

    @staticmethod
    def get_manufacturer(manufacturer_id):
        return ManufacturerDAO.get_manufacturer(manufacturer_id)

    @staticmethod
    def create_manufacturer(data):
        return ManufacturerDAO.create_manufacturer(data)

    @staticmethod
    def update_manufacturer(manufacturer_id, data):
        return ManufacturerDAO.update_manufacturer(manufacturer_id, data)

    @staticmethod
    def delete_manufacturer(manufacturer_id):
        return ManufacturerDAO.delete_manufacturer(manufacturer_id)
