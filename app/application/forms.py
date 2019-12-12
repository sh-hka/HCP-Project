from flask_wtf import FlaskForm as Form
from wtforms import (
    StringField,
    IntegerField,
    HiddenField,
    DateField,
    SelectField,
    BooleanField,
)
from wtforms.validators import (
    Length,
    NumberRange,
    DataRequired,
    Optional,
    Regexp,
    Email,
    EqualTo,
    InputRequired,
    ValidationError,
)


class AddressValidator(object):
    def __init__(self, message=None):
        if not message:
            message = u"The address must be a valid US address. Make sure that you're a complete address."
        self.message = message

    def __call__(self, form, field):
        """ Check to see if google can find the address if it can't reject """
        data = field.data
        # TODO: Implement the logic
        return


class Existence(object):
    def __init__(self, model, field, cast=str, message=None):
        if not message:
            message = u"The {field.description} value {field.data} is invalid"
        self.model = model
        self.field = field
        self.cast = cast
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(
            self.field == self.cast(field.data)).first()
        if not check:
            raise ValidationError(self.message.format(field=field))


HOUSING_TYPES = [('Other', 'Other'), ('Rent', 'Rent'), ('Own', 'Own')]
PHONE_TYPES = [('Work', 'Work'), ('Home', 'Home'), ('Cell', 'Cell'),
               ('Other', 'Other')]


class ApplicationForm(Form):
    """ A visitor wants to apply to a provider """

    provider = HiddenField(validators=[DataRequired(message="Missing Provider ID.")],
                           description="Provider UID")
    first_name = StringField(validators=[DataRequired(),
                                         Length(min=2)],
                             description="First name")
    last_name = StringField(validators=[DataRequired(),
                                        Length(min=2)],
                            description="Last name")
    initial_purchase_amt = IntegerField(
        validators=[Optional(), NumberRange(min=0)],
        description="Initial purchase amount",
    )
    address = StringField(validators=[DataRequired(),
                                      AddressValidator()],
                          description="Address")
    housing_type = SelectField(validators=[DataRequired()],
                               choices=HOUSING_TYPES,
                               description="Housing Type")
    phone = StringField(validators=[DataRequired(),
                                    Regexp(r'\d{10}')],
                        description="Phone Number")
    phone_type = SelectField(validators=[DataRequired()],
                             choices=PHONE_TYPES,
                             description="Phone Type")
    email = StringField(validators=[DataRequired(), Email()],
                        description="Email ID")
    cnf_email = StringField(
        validators=[
            DataRequired(),
            Email(),
            EqualTo("email", message="Please check you email id."),
        ],
        description="Confirm email id",
    )
    ssn = StringField(
        validators=[
            DataRequired(),
            Regexp(r'\d{9}',
                   message="Your SSN should be a nine digit number."),
        ],
        description="SSN",
    )
    dob = DateField(validators=[DataRequired(message="Make sure the date is in YYYY-MM-DD format.")], description="Date of birth")
    income = IntegerField(
        validators=[DataRequired(), NumberRange(min=0)],
        description="Monthly Net income",
    )
    accept = BooleanField(
        validators=[InputRequired()],
        description=
        "I agree to the lack of privacy policy, and terms of service.",
    )
