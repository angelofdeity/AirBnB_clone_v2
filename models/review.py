#!/usr/bin/python3
""" Review module for the HBNB project """
from .base_model import BaseModel
from . import HBNB_TYPE_STORAGE
from .base_model import Base


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes review"""
        super().__init__(*args, **kwargs)
