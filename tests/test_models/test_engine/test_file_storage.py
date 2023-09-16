#!/usr/bin/python3
"""
Unittest for file_storage.py
"""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class"""

    @classmethod
    def setUp(self):
        """ set up method """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """ tear down method """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_instantiation(self):
        """ instansiation method """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_args(self):
        """"instantiation with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all(self):
        """test all method"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        """test all method with arg"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        """
        Testing the new() method
        """
        city = City()
        state = State()
        amenity = Amenity()
        user = User()
        review = Review()
        place = Place()
        base = BaseModel()
        models.storage.new(base)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.new(place)
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn(state, models.storage.all().values())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn(user, models.storage.all().values())
        self.assertIn(review, models.storage.all().values())
        self.assertIn(place, models.storage.all().values())
        self.assertIn(base, models.storage.all().values())

    def test_new_2(self):
        """test new method"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """ test new method with none"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """
        Testing the save() method
        """
        city = City()
        state = State()
        amenity = Amenity()
        user = User()
        review = Review()
        place = Place()
        base = BaseModel()
        models.storage.new(base)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.new(place)
        models.storage.save()
        with open("file.json", "r") as file:
            f_contents = file.read()
            self.assertIn("City." + city.id, f_contents)
            self.assertIn("State." + state.id, f_contents)
            self.assertIn("Amenity." + amenity.id, f_contents)
            self.assertIn("User." + user.id, f_contents)
            self.assertIn("Review." + review.id, f_contents)
            self.assertIn("Place." + place.id, f_contents)
            self.assertIn("BaseModel." + base.id, f_contents)

    def test_reload(self):
        """test reload method"""
        city = City()
        state = State()
        amenity = Amenity()
        user = User()
        review = Review()
        place = Place()
        base = BaseModel()
        models.storage.new(base)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.new(place)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)

    def test_reload_with_arg(self):
        """test reload method with argument"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
