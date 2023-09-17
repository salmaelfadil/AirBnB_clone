#!/usr/bin/python3
"""
Module for the BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel class from which other classes will inheret"""
    def __init__(self, *args, **kwargs):
        """
        Starting point of the class
        Args:
            *args: arguments .
            **kwargs: Keys and values of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """returns a string representation of base model"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Save basemodel method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Save basemodel to dictionary function"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
