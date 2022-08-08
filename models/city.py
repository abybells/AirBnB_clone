#!/usr/bin/python3
"""
city module
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


'Module for City'


class City(BaseModel):
    'City class'

    state_id = ""
    name = ""
