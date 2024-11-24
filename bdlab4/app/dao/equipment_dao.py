# app/dao/equipment_dao.py
from ..models.equipment import Equipment
from database import db

class EquipmentDAO:
    @staticmethod
    def get_all_equipments():
        return Equipment.query.all()

    @staticmethod
    def get_equipment(equipment_id):
        return Equipment.query.get(equipment_id)

    @staticmethod
    def create_equipment(data):
        equipment = Equipment(**data)
        db.session.add(equipment)
        db.session.commit()
        return equipment

    @staticmethod
    def update_equipment(equipment_id, data):
        equipment = EquipmentDAO.get_equipment(equipment_id)
        for key, value in data.items():
            setattr(equipment, key, value)
        db.session.commit()
        return equipment

    @staticmethod
    def delete_equipment(equipment_id):
        equipment = EquipmentDAO.get_equipment(equipment_id)
        db.session.delete(equipment)
        db.session.commit()
