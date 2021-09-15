# postgreSQLalchemy

## About

This is a boiler plate Flask application which integrates PostgreSQL, Sqlalchemy, Flask-Migrate, and
blueprints.

Included are some example operations using SQLalchemy and PostgreSQL which are practical
for real world use cases.

Operations added so far
- Upsert <br>
- More to be added soon

## Setup

Coming soon
  
## Commands

For the development env
```
$ sudo docker-compose exec db psql --username=nfl --dbname=nfl_dev
$ sudo docker-compose -f docker-compose.yml down -v
$ sudo docker-compose -f docker-compose.yml up -d --build
$ sudo docker-compose -f docker-compose.yml exec web python manage.py create_db
$ sudo docker-compose -f docker-compose.yml exec web python manage.py migrate_db
$ sudo docker-compose -f docker-compose.yml exec web python manage.py upgrade_db
$ sudo docker-compose -f docker-compose.yml exec web python manage.py upsert
```

For the production env
```
$ sudo docker-compose exec db psql --username=nfl --dbname=nfl_prod
$ sudo docker-compose -f docker-compose.prod.yml down -v
$ sudo docker-compose -f docker-compose.prod.yml up -d --build
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py create_prod
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate_prod
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py upgrade_prod
$ sudo docker-compose -f docker-compose.prod.yml exec web python manage.py upsert
```
  
## Acknowledgements

Boilerplate is based off [flask-on-docker](https://github.com/testdrivenio/flask-on-docker).