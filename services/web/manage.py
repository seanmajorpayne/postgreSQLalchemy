from flask.cli import FlaskGroup

from project import app, db
from upsert.upsert import perform_upsert

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    print("creating db")
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("upsert")
def upsert_data():
    perform_upsert()

@cli.command("seed_db")
def seed_db():
    print("seeding")
    #n = NFL(game_key=1111, player="A1")
    #db.session.add(n)
    #db.session.commit()


if __name__ == "__main__":
    cli()
