import sys

from flask.cli import FlaskGroup
from application import create_app, db
from application.api.drills.models import Drill
from application.api.users.models import User



app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    db.session.add(Drill(part_number='201TESTDRILL', diameter=1, length=14, drill_depth=12, machine_type="SDS-Plus", material_type="Concrete"))
    db.session.add(Drill(part_number='202TESTDRILL', diameter=1, length=8, drill_depth=6, machine_type="3/8 Chuck", material_type="Steel"))

    db.session.add(User(username='jonny', email='jon@sessionsdev.com', password='password'))
    db.session.add(User(username='kristen', email='kristen@test.com', password='password'))
    
    db.session.commit()


if __name__ == '__main__':
    cli()
