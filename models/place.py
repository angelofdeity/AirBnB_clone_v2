#!/usr/bin/python3
""" Place Module for HBNB project """
from .base_model import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from . import HBNB_TYPE_STORAGE
from .base_model import Base


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if HBNB_TYPE_STORAGE == 'db':
        amenities = relationship(
            "Amenity", secondary="place_amenity", back_populates="place_amenities", viewonly=False)
    else:
        @property
        def amenities(self):
            from . import Amenity
            from . import storage

            amenity_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            from . import Amenity
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)
