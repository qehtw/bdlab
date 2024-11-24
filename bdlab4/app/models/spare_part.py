# app/models/spare_part.py
from database import db

class SparePart(db.Model):
    __tablename__ = 'spare_parts'

    part_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.manufacturer_id'))

    manufacturer = db.relationship('Manufacturer', back_populates='spare_parts')
    replaced_parts = db.relationship('ReplacedPart', back_populates='part')

    def to_dict(self):
        return {
            'part_id': self.part_id,
            'name': self.name,
            'manufacturer_id': self.manufacturer_id,
            'manufacturer': self.manufacturer.to_dict() if self.manufacturer else None
        }
