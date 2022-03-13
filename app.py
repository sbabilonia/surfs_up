#Load dependencies; flask, dt, numpy, pandas, sqlalchemy/addons
#Jsonify displays data in json form

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#create an engine to access SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect database into seperate classes
Base = automap_base()

#reflect tables; we can now save references to each table
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link from Python to our db
session = Session(engine)



#Flask webpage setup
app = Flask(__name__)

@app.route('/')
def welcome():
     return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes: 
    /api/v1.0/precipitation 
    /api/v1.0/stations 
    /api/v1.0/tobs 
    /api/v1.0/temp/start/end 
    ''')

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


@app.route('/api/v1.0/stations')
def stations():
    #query to get all stations in db
    results = session.query(Station.station).all()
    #unvravel results into 1D array and convert to a list
    stations = list(np.ravel(results))
    #to return our list as JSON, we need to add param: stations=stations
    return jsonify(stations=stations)

@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))

    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        #calculate temp min max avg
        #asterisk * indicates multiple query results (min, max, avg)
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
            
        temps = list(np.ravel(results))

        return jsonify(temps=temps)

    #calculate the temperature minimum, average, and maximum with the start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    temps = list(np.ravel(results))

    return jsonify(temps=temps)

if __name__ == "__main__":
    app.run(debug=True)