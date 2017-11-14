import json
from shapely.geometry import Polygon
from geoalchemy2.shape import to_shape
from models import engine, Map
from sqlalchemy.orm import sessionmaker

#to read data from map.geojson file.
'''
with open("./map.geojson") as map:
    data = json.load(map)
'''

session = sessionmaker(bind=engine)
session = session()


#To insert data into the database
'''
for feature in data['features']:
    place  = feature['properties']['name']
    parent  = feature['properties']['parent']
    coordinates  = feature['geometry']['coordinates'][0]
    geom = Polygon(coordinates).wkt
    print(geom)
    try:
        p = Map(place=place,
                parent=parent,
                geom=geom)
        session.add(p)
        session.commit()
    except Exception as e:
        session.rollback() 
        print ('Insertion unsuccessful', e)
'''

#making select query on Map database
res = session.query(Map).all()
for r in res:
    print(r.place,r.parent,to_shape(r.geom))                   