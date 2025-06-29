from models import *
from flask_smorest import Blueprint
from schemas import LoginSchema
from db import db

from flask.views import MethodView
blp=Blueprint('users', __name__,description='User related endpoints')

@blp.route('/login')
class Login(MethodView):
    @blp.response(200,LoginSchema(many=True))
    def get(self):
       pass

    @blp.arguments(LoginSchema)
    @blp.response(400, LoginSchema)
    def post(self, args):
        sd = User(**args)
        db.session.add(sd)
        db.session.commit()
        return sd

