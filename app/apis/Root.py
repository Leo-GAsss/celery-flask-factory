from app.apis import bp


@bp.route("/")
def hello():
    from app.task import add_record
    add_record.delay()
    return "success", 200
