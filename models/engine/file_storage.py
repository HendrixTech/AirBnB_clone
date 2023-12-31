#!/usr/bin/python3

"""This will be the module for FileStorage class"""
import json
import datetime
import os


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
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            d = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(d, file)

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review
                   }
        return classes

    def reload(self):
        """Returns a dictionary of valid classes and their references"""
        try:
            obj_dict = {}
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, val in obj_dict.items():
                    self.all()[key] = self.classes()[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def attributes(self):
        """Returns the valid attr and their types for classname"""
        attr = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attr
