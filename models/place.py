#!/usr/bin/python3
"""
Place module
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


'Module for Place'


class Place(BaseModel):
    'Place class'

    user_id = ""
    name = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
