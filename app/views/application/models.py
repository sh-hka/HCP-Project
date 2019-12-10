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
    initial_purchase = db.Column(db.Integer, nullable=True)
    # TODO: See if there's any better way to store address given google geo-coding
    address = db.Column(db.String, nullable=False)
    housing_type = db.Column(db.String, nullable=False, default="Other")
    phone = db.Column(db.String(length=10), nullable=False)
    phone_type = db.Column(db.String, nullable=False, default="Other")
    email = db.Column(db.String, nullable=False)
    ssn = db.Column(db.String(length=9), nullable=False)
    dob = db.Column(db.Date, nullable=False)

    def __dict__(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'initial_purchase': self.initial_purchase,
            'address': self.address,
            'housing_type': self.housing_type,
            'phone': self.phone,
            'phone_type': self.phone_type,
            'email': self.email,
            'ssn': self.ssn,
            'dob': self.dob,
        }

    def __repr__(self):
        return ('<Application {id:02d}>\n'
                'Name: {first_name} {last_name}\n'
                'Contact:\n'
                '\t{phone} ({phone_type})\n'
                '\t{email}\n'
                'Addr:\n{addr}\n'
                '</Application>'.format(
                    id=self.id,
                    first_name=self.first_name,
                    last_name=self.last_name,
                    phone=self.phone,
                    phone_type=self.phone_type,
                    email=self.email,
                    addr=self.address,
                ))
