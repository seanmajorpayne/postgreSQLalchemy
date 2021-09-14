# postgreSQLalchemy

## About

A series of difficult operations developers may need to perform
using SQLalchemy and PostgreSQL.

Operations added so far
- Upsert <br>
More information coming soon.
  
## Commands

```
$ docker-compose exec db psql --username=nfl --dbname=nfl_prod
$ docker-compose -f docker-compose.prod.yml down -v
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
$ docker-compose -f docker-compose.prod.yml exec web python manage.py upsert
```
  
## Acknowledgements

Boilerplate is based off [flask-on-docker](https://github.com/testdrivenio/flask-on-docker).