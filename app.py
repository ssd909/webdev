from flask import Flask
from flask_smorest import Blueprint
from db import db
from models import userModel
from users import blp as userBlp
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)





if __name__ == '__main__':
    app.run(debug=True)
with app.app_context():
    db.create_all()
app.register_blueprint(userBlp)