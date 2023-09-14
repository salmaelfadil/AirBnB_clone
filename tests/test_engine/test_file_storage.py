import unittest
import json
import os
from datetime import datetime
from models.base_model import BaseModel
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
