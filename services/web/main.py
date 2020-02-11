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
    db.session.add(Drill(part_number='201TESTDRILL'))
    db.session.add(Drill(part_number='202TESTDRILL'))

    db.session.add(User(username='jonny', email='jon@sessionsdev.com'))
    db.session.add(User(username='kristen', email='kristen@test.com'))
    
    db.session.commit()


if __name__ == '__main__':
    cli()
