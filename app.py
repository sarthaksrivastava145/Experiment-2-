from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airline.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

# initialising the database
db = SQLAlchemy(app)

# creating specific classes for each property
class Passenger(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    contact = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=True)
   #nationality = db.Column(db.String(100), nullable=True)

class Flight(db.Model):
    flight_no = db.Column(db.String(10), primary_key=True)
    frm = db.Column(db.String(50), nullable=False)
    too = db.Column(db.String(50), nullable=False)
    dep_date = db.Column(db.String(20), nullable=True)
    dep_time = db.Column(db.String(20), nullable=True)
    arr_date = db.Column(db.String(20), nullable=True)
    arr_time = db.Column(db.String(20), nullable=True)

class Booking(db.Model):
    pid = db.Column(db.Integer, db.ForeignKey('passenger.pid'), primary_key=True)
    flight_no = db.Column(db.String(10), db.ForeignKey('flight.flight_no'), primary_key=True)
    passenger = db.relationship('Passenger', backref=db.backref('bookings', cascade='all, delete'))
    flight = db.relationship('Flight', backref=db.backref('bookings', cascade='all, delete'))

with app.app_context():
    db.create_all()

# home page route
@app.route('/')
def index():
    return render_template('index.html')

# passenger page 
@app.route('/passengers')
def passengers():
    passengers_data = Passenger.query.order_by(Passenger.pid.desc()).all()
    return render_template('passengers.html', passengers=passengers_data)

# adding passenger
@app.route('/add_passenger', methods=['POST'])
def add_passenger():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        sex = request.form['sex']
        address = request.form['address']
        contact = request.form['contact']
        email = request.form['email']

        if name and age and sex:
            new_passenger = Passenger(name=name, age=age, sex=sex, address=address, contact=contact, email=email)
            db.session.add(new_passenger)
            db.session.commit()
            flash('Passenger added successfully!')
        else:
            flash('Please fill in all fields.')

    return redirect(url_for('passengers'))

# deleting passenger
@app.route('/delete_passenger', methods=['POST'])
def delete_passenger():
    pid = request.form['pid']
    passenger = Passenger.query.get(pid)
    if passenger:
        db.session.delete(passenger)
        db.session.commit()
        flash('Passenger deleted successfully!')
    else:
        flash('Passenger not found.')

    return redirect(url_for('passengers'))

# flight page route
@app.route('/flights')
def flights():
    flights_data = Flight.query.order_by(Flight.flight_no.desc()).all()
    return render_template('flights.html', flights=flights_data)

# adding flights
@app.route('/add_flight', methods=['POST'])
def add_flight():
    if request.method == 'POST':
        flight_no = request.form['flight_no']
        frm = request.form['from']
        to = request.form['to']
        dep_date = request.form['dep_date']
        dep_time = request.form['dep_time']
        arr_date = request.form['arr_date']
        arr_time = request.form['arr_time']

        if flight_no and frm and to:
            new_flight = Flight(flight_no=flight_no, frm=frm, too=to, dep_date=dep_date, dep_time=dep_time, arr_date=arr_date, arr_time=arr_time)
            db.session.add(new_flight)
            db.session.commit()
            flash('Flight added successfully!')
        else:
            flash('Please fill in all fields.')

    return redirect(url_for('flights'))

# deleting flights
@app.route('/delete_flight', methods=['POST'])
def delete_flight():
    flight_no = request.form['flight_no']
    flight = Flight.query.get(flight_no)
    if flight:
        db.session.delete(flight)
        db.session.commit()
        flash('Flight deleted successfully!')
    else:
        flash('Flight not found.')

    return redirect(url_for('flights'))

# booking flights
@app.route('/book', methods=['POST'])
def book_flight():
    if request.method == 'POST':
        pid = request.form['pid']
        flight_no = request.form['flight_no']

        passenger = Passenger.query.get(pid)
        flight = Flight.query.get(flight_no)

        if passenger and flight:
            new_booking = Booking(passenger=passenger, flight=flight)
            db.session.add(new_booking)
            db.session.commit()
            flash('Flight booked successfully!')
        else:
            flash('Invalid passenger ID or flight number.')

    return redirect(url_for('flights'))

# @app.route('/boarding_pass', methods=['POST'])
# def boarding_pass():
#     if request.method == 'POST':
#         pid = request.form['pid']
#         passenger = Passenger.query.get(pid)

#         if passenger and passenger.bookings:
#             booking_data = [(b.flight_no, b.flight.frm, b.flight.too, b.flight.dep_date, b.flight.dep_time) for b in passenger.bookings]
#             return render_template('boarding_pass.html', boarding=booking_data)

#         flash('No booking found for this PID.')
#         return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port=8000, debug=True)