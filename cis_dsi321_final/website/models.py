from . import db, db2
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask_restful import Resource


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    studentid = db.Column(db.String(150))
    password = db.Column(db.String(150))

class AdminUser(db2.Model, UserMixin):
    id = db2.Column(db2.Integer, primary_key=True)
    adminid = db2.Column(db2.String(150), unique=True)
    adminpassword = db2.Column(db2.String(150))

class SearchForm(FlaskForm):
     searched = StringField("searched")
     submit = SubmitField("Submit")

class companyapi(Resource):
    def get(self):
        return {"data":"pope"}
