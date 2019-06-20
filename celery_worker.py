from app import create_app, make_celery

celery = make_celery(create_app())
from app.models.account import Account
from app.extensions import db


@celery.task()
def add_together():
    a = Account(string2="he", string="11")
    db.session.add(a)
    db.session.commit()
