from app import db


class Application(db.Model):

    __tablename__ = 'applications'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True,
                   nullable=False)
    provider = db.Column(db.Integer,
                         db.ForeignKey('providers.id'),
                         nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String, nullable=False)
    housing_type = db.Column(db.String, nullable=False, default="Other")
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String(length=10), nullable=False)
    phone_type = db.Column(db.String, nullable=False, default="Other")
    ssn = db.Column(db.String(length=9), nullable=False)
    income = db.Column(db.Integer, nullable=False)
    initial_purchase = db.Column(db.Integer, nullable=True)

    def __to_dict__(self):
        return {
            'id': self.id,
            'provider': self.provider,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'dob': self.dob,
            'address': self.address,
            'housing_type': self.housing_type,
            'email': self.email,
            'phone': self.phone,
            'phone_type': self.phone_type,
            'ssn': self.ssn,
            'income': self.income,
            'initial_purchase': self.initial_purchase,
        }

    def __repr__(self):
        return self.__to_dict__().__repr__()
