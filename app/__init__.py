from flask import Flask
from celery import Celery
from app.extensions import db
from app.apis import bp

def make_celery(app):
    celery = Celery(
        app.import_name,
        # backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'],
        include=["app.task"]
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

def create_app():
    app = Flask(__name__)
    app.config.update(
        CELERY_BROKER_URL='pyamqp://guest@localhost//',
        SQLALCHEMY_DATABASE_URI='postgresql://casss@localhost/a_test'
        # CELERY_RESULT_BACKEND='redis://localhost:6379'
    )
    db.init_app(app)
    app.register_blueprint(bp)
    return app





