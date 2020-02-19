import pytest

from application import create_app, db
from application.api.drills.models import Drill


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


