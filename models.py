from sqlalchemy import create_engine as ca
from sqlalchemy import Column, String
from geoalchemy2 import Geometry

engine = ca("postgresql://postgres:postgres@localhost:5432/postgres")
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Map(Base):
    __tablename__ = 'map'

    place = Column(String, primary_key = True)
    parent = Column(String, nullable=False)
    geom = Column(Geometry('POLYGON'),nullable=False)

    def __init__(self, place, parent, geom):
        self.place = place
        self.parent = parent
        self.geom = geom

Base.metadata.create_all(engine)
