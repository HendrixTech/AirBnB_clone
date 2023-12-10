#!/usr/bin/python3
"""This module is the base model where every other class inherits from"""

import uuid
from datetime import datetime
from engine import file_storage


class BaseModel:

    """Class from which other classes inherits from"""

     def __init__(self, *args, **kwargs):
    
         if kwargs is not None and kwargs != {}:
             for key in kwargs:
                 if key == "created_at":
                     self.__dict__["created_at"] = datetime.strptime(
                         kwargs["created_at"], "%Y-%m%dT%H:%M:%S.%f"
                     )
                 elif key == "updated_at":
                     self.__dict__["updated_at"] = datetime.strptime(
                         kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                     )
                 else:
                     self.__dict__[key] = kwargs[key]
         else:
             self.id = str(uuid.uuid4())
             self.created_at = datetime.now()
             self.updated_at = datetime.now()

    def __str__(self):
        """Returns an official string representation"""

        # return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return "[{}] ({}) {}" . \
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute """

        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
