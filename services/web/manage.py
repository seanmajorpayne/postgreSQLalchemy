import subprocess
from flask.cli import FlaskGroup
from project import app, db
from upsert.upsert import perform_upsert

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    print("creating db")
    subprocess.run(['sh', './init.sh'])


@cli.command("create_prod")
def create_prod():
    print("creating prod")
    subprocess.run(['sh', './init.prod.sh'])


@cli.command("migrate_db")
def migrate_db():
    print("migrating db")
    subprocess.run(['sh', './migrate.sh'])


@cli.command("migrate_prod")
def migrate_prod():
    print("migrating prod")
    subprocess.run(['sh', './migrate.prod.sh'])


@cli.command("upgrade_db")
def upgrade_db():
    print("upgrading db")
    subprocess.run(['sh', './upgrade.sh'])


@cli.command("upgrade_prod")
def upgrade_prod():
    print("upgrading prod")
    subprocess.run(['sh', './upgrade.prod.sh'])


@cli.command("upsert")
def upsert_data():
    perform_upsert("project/static/train_player_tracking.csv")


if __name__ == "__main__":
    cli()
