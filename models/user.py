#!/usr/bin/python3
"""
user module
"""
import uuid
from datetime import datetime
from models.base_model import BaseModel


'Module for User'


class User(BaseModel):
    'User class'

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    # def __init__(self, *args, **kwargs):
    #     """initialize variables and methods"""
    #     super().__init__(self, *args, **kwargs)
