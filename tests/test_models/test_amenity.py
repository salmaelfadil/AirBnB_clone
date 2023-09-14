#!/usr/bin/python3
"""
amenity test
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    def test_str(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, Amenity))


if __name__ == "__main__":
    unittest.main()
