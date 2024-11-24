# app/models/technician.py
from database import db

class Technician(db.Model):
    __tablename__ = 'technicians'

    technician_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(255))

    repairs = db.relationship('Repair', secondary='technician_repairs', back_populates='technicians')
    schedule = db.relationship('TechnicianSchedule', back_populates='technician')

    def to_dict(self):
        return {
            'technician_id': self.technician_id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'repairs': [repair.to_dict() for repair in self.repairs]
        }

    def to_dict_basic(self):
        return {
            'technician_id': self.technician_id,
            'name': self.name
        }
