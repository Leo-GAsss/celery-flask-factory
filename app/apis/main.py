from app.apis import bp


@bp.route("/")
def hello():
    from celery_worker import add_together
    add_together.delay()
    return "success", 200
