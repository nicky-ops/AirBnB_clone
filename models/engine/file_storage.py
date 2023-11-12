#!/usr/bin/python3
import json
import os
"""
Module contains FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances.
"""


class FileStorage():
    """
    Class defines a method for storing and retriving data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        data = {}
        for k, v in FileStorage.__objects.items():
            data[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(data, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for k, v in data.items():
                    class_name, obj_id = k.split(".")
                    cls = self.get_class(class_name)
                    if cls:
                        obj = cls(**v)
                        self.new(obj)

    def get_class(self, class_name):
        """
        Define a method to get a class by its name
        """
        if class_name == "User":
            return User
        elif class_name == "Place":
            return Place
        elif class_name == "State":
            return State
        elif class_name == "City":
            return City
        elif class_name == "Amenity":
            return Amenity
        elif class_name == "Review":
            return Review
        return None
