# Celery-Flask-Factory

A demo of using celery in Flask with
 [Application Factories](http://flask.pocoo.org/docs/1.0/patterns/appfactories/).
 
## Get started

1. Set up the virtualenv:

    ```bash
    pipenv install
    ```
    
2. Refer [here](https://www.postgresql.org/docs/11/tutorial-start.html) to configure and start PostgreSQL service.

    You can also find a more detailed tutorial at [ArchWiki](https://wiki.archlinux.org/index.php/PostgreSQL).

3. Refer [here](https://www.rabbitmq.com/download.html) to install and start RabbitMQ.

4. Initialize the database.

    ```bash
    flask initdb
    ```

5. Kickoff a celery worker:

    ```bash2
    celery -A app.celery worker
    ```

6. Run flask sever:

    ```bash
    flask run
    ```