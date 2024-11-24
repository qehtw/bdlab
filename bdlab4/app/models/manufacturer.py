# app/models/manufacturer.py
from database import db

class Manufacturer(db.Model):
    __tablename__ = 'manufacturers'

    manufacturer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    spare_parts = db.relationship('SparePart', back_populates='manufacturer')
    equipment = db.relationship('Equipment', back_populates='manufacturer')

    def to_dict(self):
        return {
            'manufacturer_id': self.manufacturer_id,
            'name': self.name,
        }
