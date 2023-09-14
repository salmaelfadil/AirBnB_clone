#!/usr/bin/python3
"""test the City method"""
import unittest
from models.base_model import BaseModel
from models.city import City
import models


class TestCity(unittest.TestCase):
    """Test the City module"""

    def test_city_class(self):
        """
        some city tests
        """
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")

    def test_city_b(self):
        """
        city tests
        """
        self.assertTrue(issubclass(City, BaseModel))
        self.assertEqual(City, type(City()))

    def test_city_check(self):
        """some checks"""
        self.assertIn(City(), models.storage.all().values())
        self.assertEqual(str, type(City().id))

    def test_all_instances(self):
        """
        test instances
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_cities_unique_ids(self):
        """
        test unique ids
        """
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_args_unused(self):
        """
        test unused args
        """
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_save(self):
        """
        test save cities and check updated_at
        """
        city = City()
        old_save = city.updated_at
        city.save()
        new_save = city.updated_at
        self.assertNotEqual(old_save, new_save)


if __name__ == "__main__":
    unittest.main()
