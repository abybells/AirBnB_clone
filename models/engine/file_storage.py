#!/usr/bin/python3
"""File Storage for AirBnb Console"""
import json
from os import path
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City


class FileStorage():
    """Defines a Class for Filestorage"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file """
        temp = dict()
        for keys in self.__objects.keys():
            temp[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, mode='w') as json_file:
            json.dump(temp, json_file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        exists ; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)
        """

        MODELS = [Amenity, BaseModel, City, Place, Review, State, User]

        if path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r', encoding='utf-8') as json_file:
                deserialize = json.load(json_file)
            for key in deserialize.keys():
                for model in MODELS:
                    if model.__name__ == deserialize[key]["__class__"]:
                        self.__objects[key] = model(**deserialize[key])
        else:
            with open(self.__file_path, "w", encoding='utf-8') as json_file:
                json.dump({}, json_file)
            self.reload()
