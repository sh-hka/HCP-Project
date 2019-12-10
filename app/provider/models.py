from app import db


class Provider(db.Model):

    __tablename__ = 'providers'

    id = db.Column(db.Integer,
                   nullable=False,
                   autoincrement=True,
                   primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    speciality = db.Column(db.String)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    zip = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)

    __table_args__ = (
        db.CheckConstraint(-90 <= lat, name="Latitude lower range check"),
        db.CheckConstraint(lat <= 90, name="Latitude upper range check"),
        db.CheckConstraint(-180 <= lng, name="Longitude lower range check"),
        db.CheckConstraint(lng <= 180, name="Longitude upper range check"),
        {},
    )
