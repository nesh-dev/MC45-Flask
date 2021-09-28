from flask import Blueprint 
from flask_restful import Api 
from .views.auth import (RegisterResource, LoginResource)

apiv1 = Blueprint('apiv1', __name__)

api = Api(apiv1, prefix='/api/v1')



api.add_resource(RegisterResource, '/register')
api.add_resource(LoginResource, '/login')
# api.add_resource(LogoutResource, '/logout')



