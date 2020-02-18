from application import db
from application.api.drills.models import Drill


def find_drill(diameter, depth, machine, material):

    _query = Drill.query

    print(diameter, depth, machine, material)

    if diameter:
        _query = _query.filter_by(diameter=diameter)

    if depth:
        _query = _query.filter_by(drill_depth=depth)

    if machine:
        _query = _query.filter_by(machine_type=machine)

    if material:
        _query = _query.filter_by(material_type=material)

    print(_query)

    drill = _query.all()
    return drill
