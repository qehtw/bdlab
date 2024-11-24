# app/dao/repair_dao.py
from ..models.repair import Repair
from database import db

class RepairDAO:
    @staticmethod
    def get_all_repairs():
        return Repair.query.all()

    @staticmethod
    def get_repair(repair_id):
        return Repair.query.get(repair_id)

    @staticmethod
    def create_repair(data):
        repair = Repair(**data)
        db.session.add(repair)
        db.session.commit()
        return repair

    @staticmethod
    def update_repair(repair_id, data):
        repair = RepairDAO.get_repair(repair_id)
        for key, value in data.items():
            setattr(repair, key, value)
        db.session.commit()
        return repair

    @staticmethod
    def delete_repair(repair_id):
        repair = RepairDAO.get_repair(repair_id)
        db.session.delete(repair)
        db.session.commit()
