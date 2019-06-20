#  -*- coding: utf-8 -*-

import click
from celery import Celery
from flask import Flask

from app.apis import bp
from app.extensions import db
from app.models.Record import Record


def make_celery(app):
    celery = Celery(
        app.import_name,
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
        SQLALCHEMY_DATABASE_URI='postgresql://your_username@localhost/your_db',
    )
    db.init_app(app)
    register_commands(app)
    app.register_blueprint(bp)
    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Drop before creating database.')
    def initdb(drop):
        """
        Initialize the database.
        """
        if drop:
            click.confirm(
                'This operation will delete the database, do you want to continue?',
                abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo(app.config['SQLALCHEMY_DATABASE_URI'])
        click.echo('Initialized database.')


celery = make_celery(create_app())
