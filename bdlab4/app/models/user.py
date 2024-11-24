# app/models/user.py
from database import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(255))
    address = db.Column(db.Text)

    equipment = db.relationship('UserEquipment', back_populates='user')

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address,
        }
