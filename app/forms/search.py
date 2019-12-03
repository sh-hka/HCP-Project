from flask_wtf import FlaskForm as Form
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import Length, NumberRange, DataRequired


class Search(Form):
    """ User wants to search for a provider. """

    query = StringField(validators=[Length(max=140)], description="Search")
    lat = FloatField(
        validators=[DataRequired(), NumberRange(min=-90, max=90)], description="Latitude"
    )
    lng = FloatField(
        validators=[DataRequired(), NumberRange(min=-180, max=180)], description="Longitude"
    )
    search_range = IntegerField(
        validators=[NumberRange(min=1, max=500)], description="Range"
    )
