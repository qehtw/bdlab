from flask import Flask
from database import db
from app.controllers.user_controller import user_bp
from app.controllers.manufacturer_controller import manufacturer_bp
from app.controllers.equipment_controller import equipment_bp
from app.controllers.spare_part_controller import spare_part_bp
from app.controllers.technician_controller import technician_bp
from app.controllers.repair_type_controller import repair_type_bp
from app.controllers.user_equipment_controller import user_equipment_bp
from app.controllers.repair_controller import repair_bp
from app.controllers.replaced_part_controller import replaced_part_bp
from app.controllers.technician_schedule_controller import technician_schedule_bp
from app.controllers.technician_repairs_controller import technician_repairs_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/dblab'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Розгортання Blueprints
app.register_blueprint(user_bp)
app.register_blueprint(manufacturer_bp)
app.register_blueprint(equipment_bp)
app.register_blueprint(spare_part_bp)
app.register_blueprint(technician_bp)
app.register_blueprint(repair_type_bp)
app.register_blueprint(user_equipment_bp)
app.register_blueprint(repair_bp)
app.register_blueprint(replaced_part_bp)
app.register_blueprint(technician_schedule_bp)
app.register_blueprint(technician_repairs_bp)

if __name__ == '__main__':
    app.run(debug=True)
