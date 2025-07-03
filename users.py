from models import *
from flask_smorest import Blueprint
from schemas import LoginSchema
from db import db
import bcrypt
from flask import jsonify

from flask.views import MethodView
blp=Blueprint('users', __name__,description='User related endpoints')

@blp.route('/login')
class Login(MethodView):
    @blp.response(200,LoginSchema(many=True))
    def get(self):
       return User.query.all()

    @blp.arguments(LoginSchema)
    @blp.response(201, LoginSchema)
    def post(self, args):
        sd = User(**args)

        user_hs=bcrypt.hashpw(sd.password.encode('utf-8'), bcrypt.gensalt())
        sd.password = user_hs
        db.session.add(sd)
        db.session.commit()
        return sd
@blp.route('/was/<int:id>')
class Delete(MethodView):


    @blp.response(201, LoginSchema)
    def delete(self, id):
        sd=User.query.get_or_404(id)
        db.session.delete(sd)
        db.session.commit()
        return sd

