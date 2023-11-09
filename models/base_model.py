#!/usr/bin/python3
from datetime import datetime
import uuid
from models import storage
"""
This class BaseModel takes care of the initializaion, serialization and deserialization of class instances.
It defines all common attributes/methods for other classes
"""


class BaseModel():
    """
    Base class defines all common attributes/methods for other classes to inherit
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        defines string representation of an object
        """
        return("{} {} {}".format(__class__.__name__,self.id, self.__dict__))

    def save(self):
        """
        updates public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        class_name = __class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = class_name
        return obj_dict
