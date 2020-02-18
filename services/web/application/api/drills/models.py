from sqlalchemy.sql import func

from application import db


class Drill(db.Model):
    __tablename__ = "drills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    part_number = db.Column(db.String(128), nullable=False)
    diameter = db.Column(db.Integer)
    length = db.Column(db.Integer)
    drill_depth = db.Column(db.Integer)
    machine_type = db.Column(db.String)
    material_type = db.Column(db.String)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, part_number, diameter, length, drill_depth, machine_type, material_type):
        self.part_number = part_number
        self.diameter = diameter
        self.length = length
        self.drill_depth = drill_depth
        self.machine_type = machine_type
        self.material_type = material_type


    
class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        
