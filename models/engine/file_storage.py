#!/usr/bin/python3
"""
File_storage class
This module contains the FileStorage class
which is responsible for
storing and retrieving objects in JSON format.
"""
import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """Represents file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects obj with key <obj_class_name>.id
        Args:
            obj: The obj to be added to the storage
        """
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Save to json file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for val in obj_dict.values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            return
