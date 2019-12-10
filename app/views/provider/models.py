from app import db


class Provider(db.Model):

    __tablename__ = 'providers'

    id = db.Column(db.Integer, nullable=False, autoincrement=True)

