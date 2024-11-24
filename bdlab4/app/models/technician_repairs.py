from database import db

class TechnicianRepairs(db.Model):
    __tablename__ = 'technician_repairs'

    technician_repair_id = db.Column(db.Integer, primary_key=True)
    technician_id = db.Column(db.Integer, db.ForeignKey('technicians.technician_id'), nullable=False)
    repair_id = db.Column(db.Integer, db.ForeignKey('repairs.repair_id'), nullable=False)

    technician = db.relationship('Technician', backref='technician_repairs')
    repair = db.relationship('Repair', backref='technician_repairs')

    def to_dict(self):
        return {
            "technician_id": self.technician_id,
            "repair_id": self.repair_id,
            "technician": self.technician.to_dict() if self.technician else None,
            "repair": self.repair.to_dict() if self.repair else None
        }
