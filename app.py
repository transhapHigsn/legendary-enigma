from flask import Flask, request, jsonify
from models import engine, Map
from sqlalchemy.orm import sessionmaker
from shapely.geometry import Point, LinearRing
from geoalchemy2.shape import to_shape

app = Flask(__name__)

session = sessionmaker(bind = engine)
session = session()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
       
@app.route('/geo_location')
def getSelf():
    data = request.json
    if data:
        lat = float(data['latitude'])
        lon = float(data['longitude'])
        p = Point(lat, lon)
        res = session.query(Map).all()
        for r in res:
            poly = to_shape(r.geom)
            line = LinearRing(list(poly.exterior.coords))
            if poly.contains(p):
                return jsonify(location=r.place)
            elif poly.touches(p):
                return jsonify(location=r.place)
            elif poly.touches(line):
                return jsonify(location=r.place)
            elif line.contains(p):
                return jsonify(location=r.place)    
        else:            
            return jsonify(location='Not present')
    else:    
        return jsonify(location='Not implemented')