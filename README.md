## MusaitTask

___

* Git clone project
* python -m venv venv
* source venv/bin/activate and .\venv\Scripts\activate
* Installing requirements.txt

      pip install -r requirements.txt
* python manage.py
* Alembic init

        alembic init migrations
* env.py files database url is given
* Alembic migrations

        alembic revision --autogenerate -m "Create tables"
* Alembic upgrade

        alembic upgrade head
