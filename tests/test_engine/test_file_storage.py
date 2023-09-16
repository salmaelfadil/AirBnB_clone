#!/usr/bin/env python3
"""
Testing File_Storage module
"""
import unittest
import json
import os
from datetime import datetime
from models.base_model import BaseModel
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage as models_storage


class TestFileStorage(unittest.TestCase):
    """Unit tests for FileStorage class"""
    def setUp(self):
        """Set up method"""
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """Tears down test methods."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """instantiation test"""
        self.assertEqual(type(self.storage), FileStorage)

    def test_init_arg(self):
        """test instantiation with arg"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    @classmethod
    def setup(cls):
        """
        Preps for testing
        """
        try:
            os.rename("file.json", "tmp")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """
        Restoring file
        """
        try:
            os.remove("file.json")
        except Exception:
            pass
        try:
            os.rename("tmp", "file.json")
        except Exception:
            pass

    def test_inst(self):
        """
        Testing instance type
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_storage_all(self):
        """
        Testing the all() method
        """
        storage = FileStorage()
        dic = storage.all()
        self.assertIsInstance(dic, dict)

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

    def test_all_method(self):
        """Tests the return type of all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_all_with_arg(self):
        """tests all method with argument"""
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_new_method(self):
        """Test for new method"""
        self.storage.new(self.model)
        self.assertIn("BaseModel." + self.model.id, self.storage.all().keys())

    def test_new_with_args(self):
        """test for new method with argument"""
        with self.assertRaises(TypeError):
            self.storage.new(self.model, 1)

    def test_reload(self):
        """test reload method"""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + self.model.id, objs)


if __name__ == "__main__":
    unittest.main()
