from flask_wtf import FlaskForm as Form
from wtforms import StringField, IntegerField, FloatField, DateField, SelectField, BooleanField
from wtforms.validators import Length, NumberRange, DataRequired, Optional, Regexp, Email, EqualTo, InputRequired


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


HOUSING_TYPES = [('Other', 'Other'), ('Rent', 'Rent'), ('Own', 'Own')]
PHONE_TYPES = [('Work', 'Work'), ('Home', 'Home'), ('Cell', 'Cell')]


class Application(Form):
    """ A visitor wants to apply to a provider """

    first_name = StringField(validators=[DataRequired(), Length(min=2)], description="First name")
    last_name = StringField(validators=[DataRequired(), Length(min=2)], description="Last name")
    initial_purchase_amt = FloatField(validators=[Optional(), NumberRange(min=0)], description="Initial purchase amount")
    address = StringField(validators=[DataRequired(), AddressValidator()], description="Address")
    housing_type = SelectField(validators=[DataRequired()], choices=HOUSING_TYPES, description="Housing Type")
    phone = StringField(validators=[DataRequired(), Regexp(r'\d{10}')], description="Phone Number")
    phone_type = SelectField(validators=[DataRequired()], choices=PHONE_TYPES, description="Phone Type")
    email = StringField(validators=[DataRequired(), Email()], description="Email ID")
    cnf_email = StringField(validators=[DataRequired(), Email(), EqualTo("email", message="Please check you email id.")], description="Confirm email id")
    ssn = StringField(validators=[DataRequired(), Regexp(r'\d{9}', message="Your SSN should be a nine digit number.")], description="SSN")
    dob = DateField(validators=[DataRequired()], description="Date of birth")
    income = IntegerField(validators=[DataRequired(), NumberRange(min=0)], description="Monthly Net income")
    accept = BooleanField(validators=[InputRequired()], description="Do you agree to our lack of privacy policy and terms of service?")


