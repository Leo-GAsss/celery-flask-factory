from app import celery
from app.extensions import db
from app.models.Record import Record


@celery.task()
def add_record():
    record = Record()
    db.session.add(record)
    db.session.commit()
