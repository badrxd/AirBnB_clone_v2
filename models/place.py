#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'	
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(Strng(1024))
    number_rooms = Column(Integer, nullable=False, defult=0)
    number_bathrooms = Column(Integer, nullable=False, defult=0)
    max_guest = Column(Integer, nullable=False, defult=0)
    price_by_night = Column(Integer, nullable=False, defult=0)
    latitude = Colmun(Float)
    longitude = Colmun(Float)
    amenity_ids = []
