import pytest

from application import create_app, db
from application.api.drills.models import Drill
from application.api.users.models import User


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("application.config.TestingConfig")
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def add_drill():
    def _add_drill(part_number):
        drill = Drill(part_number=part_number)
        db.session.add(drill)
        db.session.commit()
        return drill

    return _add_drill


@pytest.fixture(scope="function")
def add_user():
    def _add_user(username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user
