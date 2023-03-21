#!/usr/bin/python3
""" Review module for the HBNB project """
from .base_model import BaseModel
from . import HBNB_TYPE_STORAGE
from .base_model import Base


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey(places.id), nullable=False)
    user_id = Column(String(60), ForeignKey(users.id), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
