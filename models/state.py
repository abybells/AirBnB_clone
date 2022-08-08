#!/usr/bin/python3
import uuid
from datetime import datetime
from models.base_model import BaseModel


'Module for State'


class State(BaseModel):
    """ State class """

    name = ""
    
    # def __init__(self, *args, **kwargs):
    #     """initialize variables and methods"""
    #     super().__init__(self, *args, **kwargs)
