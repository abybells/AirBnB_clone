#!/usr/bin/python3
"""Define the Class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Public Attribute for the class Amenity
    Attribute:
        name: (str) - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Init method for User class
        Attributes:
            args (list): The list of arguments
            kwargs (dict): The dictionary with arguments
        """
        super().__init__(*args, **kwargs)
