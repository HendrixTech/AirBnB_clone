#!/usr/bin/python3

"""This will be the module for FileStorage class"""
import json
import datetime


class FileStorage:

    """This class stores and retrieve data

    Private class attributes
    """
    __file_path = "file.json"
    __objects = {}

    """Public instance methods"""
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d,f)
