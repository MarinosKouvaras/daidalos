from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import PilotForm, FlightForm
from app.models import Pilot, Flight
from app.database import db_session



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pilots', methods = ['GET'])
def show_pilots():
    pilots = Pilot.query.all()
    return render_template('pilots.html', pilots=pilots)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    

@app.route('/pilot-register', methods = [ 'POST', 'GET'])
def insert_pilot():
    form = PilotForm()
    message = "ENTER A PILOT"   
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        typeRate = form.typeRate.data
        instructorCategory = form.instructorCategory.data
        pilot = Pilot(name=name, surname=surname, typeRate=typeRate, instructorCategory=instructorCategory)
        db_session.add(pilot)
        db_session.commit()
        flash('Pilot register for name: {}, surname: {}'.format(
            form.name.data, form.surname.data))
        return redirect(url_for("show_pilots"))
         
           
    return render_template('pilot_form.html', form=form, message=message)

@app.route('/flight-entry/<uid>', methods = [ 'GET', 'POST'])
def insert_flight_form(uid):
    pilot = Pilot.query.filter(Pilot.id == uid).first()
    form = FlightForm(pilot=pilot)
    message = "ENTER FLIGHT"
    if form.validate_on_submit():
        date = form.date.data
        flightType = form.flightType.data
        takeoff = form.takeoff.data
        flightDuration = form.flightDuration.data
        landings = form.landings.data
        SFO = form.SFO.data
        missionAccomplished = form.missionAccomplished.data
        #flight = Flight(date=date, pilot=pilot, flightType=flightType, takeoff=takeoff, flightDuration=flightDuration, landings=landings, SFO=SFO, missionAccomplished=missionAccomplished)
        flight = Flight(date=date, flightType=flightType, takeoff=takeoff, flightDuration=flightDuration, landings=landings, SFO=SFO, missionAccomplished=missionAccomplished, pilot=pilot)
        db_session.add(flight)
        db_session.commit()
        #flights = pilot.flights
        flash('Flight Entered')
        return redirect(url_for("show_flights"))
    return render_template('flight_form.html', form=form, message=message)

@app.route("/flights/<pilot_id>", methods=["GET"])
def show_pilot_flights(pilot_id):
    pilot = Pilot.query.filter(Pilot.id == pilot_id).first()
    flights = pilot.flights
    return render_template("pilot_flights.html", pilot=pilot, flights=flights)

@app.route("/flights", methods=["GET"])
def show_flights():
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/pilots/<int:pilot_id>", methods=["GET", "POST"])
def show_pilot_form_update(pilot_id):
    message = "Modify Pilot"
    pilot = Pilot.query.filter(Pilot.id == pilot_id).first()
    if not pilot:
        return render_template("404.html", title="404"), 404
    form = PilotForm(obj=pilot)
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        typeRate = form.typeRate.data
        instructorCategory = form.instructorCategory.data
        pilot.name = name
        pilot.surname = surname
        pilot.tupeRate = typeRate
        pilot.instructorCategory = instructorCategory
        db_session.commit()
        return redirect(url_for("show_pilots"))
    return render_template("pilot_form.html", form=form, message=message, pilot=pilot)


@app.route("/flight/<int:pilot_id>/<int:flight_id>", methods=["GET", "POST"])
def show_flight_form_update(pilot_id,flight_id):
    message = "Modify Flight"
    flight = Flight.query.filter(Flight.id == flight_id).first()
    if not flight:
        return render_template("404.html", title="404"), 404
    form = FlightForm(obj=flight)
    if form.validate_on_submit():
        date = form.date.data
        #pilot = form.pilot.data
        flightType = form.flightType.data
        takeoff = form.takeoff.data
        flightDuration = form.flightDuration.data
        landings = form.landings.data
        SFO = form.SFO.data
        missionAccomplished = form.missionAccomplished.data
        flight.date = date
        #flight.pilot = pilot
        flight.flightType = flightType
        flight.takeoff = takeoff
        flight.flightDuration = flightDuration
        flight.landings = landings
        flight.SFO = SFO
        flight.missionAccomplished = missionAccomplished
        db_session.commit()
        return redirect(url_for("show_pilot_flights", pilot_id=pilot_id))
    return render_template("flight_form.html", form=form, message=message, flight=flight)

@app.route("/ifr", methods = ['GET'])
def ifr_flights():
    ifr_flights = Flight.query.filter(Flight.flightType == "IFR")
    total_flights = 0
    total_hours = 0
    total_landings = 0
    for ifr in ifr_flights:
        total_hours += ifr.flightDuration
        total_landings += ifr.landings
        total_flights += 1
    return render_template("ifr.html", ifr_flights=ifr_flights, total_hours=total_hours, total_landings=total_landings, total_flights=total_flights)

@app.route("/vfr", methods = ['GET'])
def vfr_flights():
    vfr_flights = Flight.query.filter(Flight.flightType == "VFR")
    total_flights = 0
    total_hours = 0
    total_landings = 0
    for vfr in vfr_flights:
        total_hours += vfr.flightDuration
        total_landings += vfr.landings
        total_flights += 1
    return render_template("vfr.html", vfr_flights=vfr_flights, total_hours=total_hours, total_landings=total_landings, total_flights=total_flights)