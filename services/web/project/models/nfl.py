from project import db
from sqlalchemy.sql import func


class NFL(db.Model):
    __tablename__ = "nfl"
    game_key = db.Column(db.Integer, primary_key=True, unique=False)
    play_id = db.Column(db.Integer, unique=False)
    player = db.Column(db.String(10), primary_key=True, unique=False)
    time = db.Column(db.DateTime, primary_key=True, unique=False, server_default=func.now())
    x = db.Column(db.Float, unique=False)
    y = db.Column(db.Float, unique=False)
    s = db.Column(db.Float, unique=False)
    a = db.Column(db.Float, unique=False)
    dis = db.Column(db.Float, unique=False)
    o = db.Column(db.Float, unique=False)
    dir = db.Column(db.Float, unique=False)
    event = db.Column(db.String(100), nullable=True, unique=False)

    __table_args__ = (db.UniqueConstraint("game_key", "player", "time"),)