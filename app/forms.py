from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField, SubmitField, SelectField,TimeField, DateField, DecimalField, BooleanField
from wtforms.validators import DataRequired, Length
from datetime import time
from app.models import Pilot

AIRCRAFT_TYPE = ["P2002", 'T-41']
FLIGHT_TYPE = ["VFR","IFR"]
default_time = time(7, 0)


class PilotForm(FlaskForm):
    #id = IntegerField("Id", validators=[DataRequired()])
    name = StringField("Pilot Name", validators=[DataRequired(), Length(3, 40)])
    surname = StringField("Pilot Surname", validators=[DataRequired(), Length(3, 40)])
    typeRate = SelectField("Pilot Typerate", choices=[(type) for type in AIRCRAFT_TYPE])
    instructorCategory = StringField("Pilot Instructor Category", validators=[DataRequired(), Length(1, 40)])    
    submit = SubmitField("Submit")
    
class FlightForm(FlaskForm):
    #id = IntegerField("Id", validators=[DataRequired()])
    date = DateField("Flight Date", validators=[DataRequired()])
    #pilot = StringField("Pilot Name", validators=[DataRequired(), Length(3, 40)])
    flightType = SelectField("Flight Type", choices=[(type) for type in FLIGHT_TYPE])
    takeoff = TimeField('Takeoff', format="%H:%M", validators=[DataRequired()], default=default_time)
    flightDuration = DecimalField("Flight Duration", rounding=None, validators=[DataRequired()])    
    landings = IntegerField("Number of Landings", validators=[DataRequired()])
    SFO = IntegerField("Number of SFO", validators=[DataRequired()])
    missionAccomplished = BooleanField("Mission Accomplished", validators=[DataRequired()])
    submit = SubmitField("Submit")