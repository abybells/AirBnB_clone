#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

'Module for BaseModel'

format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    'BaseModel class'
    def __init__(self, *args, **kwargs):
        'initialize data'
        if len(kwargs) is not 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                format)
        else:
            self.id = str(uuid.uuid1())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        'save method'
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        'str method'
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def to_json(self):
        'to json method'
        new_dict = self.__dict__.copy()
        for key, value in new_dict.items():
            if isinstance(value, (datetime, uuid.UUID, tuple, set)):
                if type(value) is datetime:
                    value = value.isoformat()
                new_dict.update({key: str(value)})
        new_dict['__class__'] = str(self.__class__.__name__)
        return new_dict
