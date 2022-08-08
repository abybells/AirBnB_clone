#!/usr/bin/python3
"""
Review module
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


'Module for Review'


class Review(BaseModel):
    'Review class'

    place_id = ""
    user_id = ""
    text = ""
