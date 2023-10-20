#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os

HBNB_TYPE_STORAGE = os.environ.get("HBNB_TYPE_STORAGE")
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id')),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'))
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    if HBNB_TYPE_STORAGE == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []
        reviews = relationship('Review', cascade="all, delete,\
                            delete-orphan", backref='place')
        amenities = relationship('Amenity',
                                 back_populates='place_amenities',
                                 secondary=place_amenity,
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            from models import storage
            listen = []
            for amenity_id in self.amenity_ids:
                dict_ = storage.all(storage.classes['Amenity'])\
                    .get("Amenity.{}".format(amenity_id))
                if dict_:
                    listen.append(dict_)
            return listen

        @amenities.setter
        def amenities(self, obj):
            if obj.__class__.__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)

        @property
        def reviews(self):
            """Returns the reviews of Place"""
            from models import storage
            reviews = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews.append(value)
            return reviews
