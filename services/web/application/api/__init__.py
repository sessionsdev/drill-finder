from flask_restplus import Api

from application.api.drills.views import drills_namespace
from application.api.ping import ping_namespace
from application.api.users.views import users_namespace

api = Api(version="1.0", title="Users API", doc="/doc/")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(users_namespace, path="/users")
api.add_namespace(drills_namespace, path="/drills")