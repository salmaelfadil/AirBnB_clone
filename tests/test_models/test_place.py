#!/usr/bin/python3
"""
place model unit tests
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
import models


class Test_Place(unittest.TestCase):
    """
    test Place model
    """
    def test_str_repr(self):
        """
        testing string representation
        """
        place = Place()
        cls = place.__class__.__name__
        id_ = place.id
        str_format = "[{}] ({}) {}".format(cls, id_, place.__dict__)
        self.assertEqual(place.__str__(), str_format)

    def test_place_class(self):
        """
        test place class
        """
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance_place(self):
        """test instance of place"""
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))


if __name__ == "__main__":
    unittest.main()
