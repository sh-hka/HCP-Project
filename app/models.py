from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from app import db, bcrypt


class User(db.Model, UserMixin):
    """ A user who has an account on the website. """

    __tablename__ = "users"

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    confirmation = db.Column(db.Boolean)
    _password = db.Column(db.String)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def _get_password(self):
        # Hopefully this is salted and hashed
        # TODO: Check to see if this is hashed or not.
        return self.password

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    password = db.synonym('_password', descriptor=property(_get_password,_set_password))

    def get_id(self):
        return self.email

