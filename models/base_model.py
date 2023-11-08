#!/usr/bin/python3
from datetime import datetime
import uuid
"""
This class BaseModel takes care of the initializaion, serialization and deserialization of class instances.
It defines all common attributes/methods for other classes
"""


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def __str__(self):
        print("{} {} {}".format(__class__.__name__,self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        class_name = __class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = class_name
        return obj_dict


"""Fot testing only should be removed!"""
obj = BaseModel()
obj1 = BaseModel()
obj2 = BaseModel()
print(obj1.created_at)
obj1.save()
print(obj1.updated_at)
print(obj1.to_dict())
