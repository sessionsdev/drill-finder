from flask import Blueprint, request
from flask_restplus import Api, Resource, fields, Namespace

from application import db
from application.api.drills.models import Drill

drills_namespace = Namespace("drills")


drill = drills_namespace.model(
    "Drill",
    {
        "id": fields.Integer(readOnly=True),
        "part_number": fields.String(required=True),
        "active": fields.Boolean,
        "created_date": fields.DateTime,
    },
)


class DrillsList(Resource):
    @drills_namespace.marshal_with(drill, as_list=True)
    def get(self):
        return Drill.query.all()

    @drills_namespace.expect(drill, validate=True)
    def post(self):
        post_data = request.get_json()
        part_number = post_data.get("part_number")
        response_object = {}

        drill = Drill.query.filter_by(part_number=part_number).first()

        if drill:
            response_object["message"] = "Sorry. That part number already exists."
            return response_object, 400

        db.session.add(Drill(part_number=part_number))
        db.session.commit()
        response_object = {"message": f"{part_number} was added successfully!"}
        return response_object, 201


class Drills(Resource):
    @drills_namespace.marshal_with(drill)
    def get(self, drill_id):
        drill = Drill.query.filter_by(id=drill_id).first()
        if not drill:
            drills_namespace.abort(404, f"Drill {drill_id} not found")
        return drill, 200


drills_namespace.add_resource(DrillsList, "")
drills_namespace.add_resource(Drills, "/<int:drill_id>")
