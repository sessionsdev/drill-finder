from sqlalchemy.sql import func

from application import db


class Drill(db.Model):
    __tablename__ = "drills"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    part_number = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, part_number):
        self.part_number = part_number
