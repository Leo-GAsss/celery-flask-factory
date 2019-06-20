from app.extensions import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String)
    string2 = db.Column(db.String)