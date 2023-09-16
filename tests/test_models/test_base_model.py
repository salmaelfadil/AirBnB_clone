#!/usr/bin/python3
"""
testing basemodel module
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
import json
import models
import os


class TestBaseModel(unittest.TestCase):
    """
    unittests to base model
    """
    def test_Attributes(self):
        """
        test attributes
        """
        bm_1 = BaseModel()
        bm_2 = BaseModel()
        self.assertNotEqual(bm_1.id, bm_2.id)
        self.assertEqual(BaseModel, type(BaseModel()))
        self.assertIsInstance(bm_1.id, str)

    def test_datetime(self):
        """
        test datetime
        """
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str(self):
        """test string output from BaseModel"""
        base = BaseModel()
        cls = type(base).__name__
        str_format = "[{}] ({}) {}".format(cls, base.id, base.__dict__)
        self.assertEqual(base.__str__(), str_format)

    def test_types(self):
        """
        test types
        """
        bm = BaseModel()
        self.assertTrue(type(bm), object)
        self.assertTrue(isinstance(bm, BaseModel))

    def test_save0(self):
        """
        test save
        """
        bm_2 = BaseModel()
        bm_2.save()
        bm_2id = "BaseModel." + bm_2.id
        with open("file.json", "r") as f:
            self.assertIn(bm_2id, f.read())

    def test_save1(self):
        """
        test save
        """
        bm_4 = BaseModel()
        bm_4.first_name = "Esraa"
        bm_4.save()
        self.assertNotEqual(bm_4.created_at, bm_4.updated_at)

    def test_to_dict(self):
        """
        test dict
        """
        bm_5 = BaseModel()
        dict_5 = bm_5.to_dict()
        self.assertIsInstance(dict_5, dict)
        self.assertEqual(bm_5.to_dict()["id"], bm_5.id)
        self.assertEqual(bm_5.to_dict()["__class__"], "BaseModel")
        bm_5.save()
        dict_2 = bm_5.to_dict()
        self.assertNotEqual(dict_5["updated_at"], dict_2["updated_at"])

    def test_to_dict(self):
        """
        test to_dict function from basemodel
        """
        base = BaseModel()
        prev_time = base.updated_at
        self.assertDictEqual(base.to_dict(),
                             {'__class__': type(base).__name__,
                              'updated_at': base.updated_at.isoformat(),
                              'id': base.id,
                              'created_at': base.created_at.isoformat()})
        base.save()
        self.assertNotEqual(prev_time, base.updated_at)

    def test_None_BaseModel(self):
        """
        no attributes
        """
        bm_3 = BaseModel(None)
        self.assertNotIn(None, bm_3.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        test kwargs
        """
        date_t = datetime.today()
        date_t_iso = date_t.isoformat()
        bm = BaseModel(id="567", created_at=date_t_iso, updated_at=date_t_iso)
        self.assertEqual(bm.id, "567")
        self.assertEqual(bm.created_at, date_t)
        self.assertEqual(bm.updated_at, date_t)

    def test_instantiation_with_None_kwargs(self):
        """
        test no kwargs
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModel_to_dict(unittest.TestCase):
    """
    test basemodel to dict
    """
    def test_to_dict_type(self):
        """
        test type dict
        """
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """
        test to dict
        """
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """
        test added attrs
        """
        bm = BaseModel()
        bm.name = "ALX"
        bm.my_number = 68
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_datetime_attr_if_strs(self):
        """
        test datetime
        """
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_dict_output(self):
        """
        test the output
        """
        dt = datetime.today()
        bm = BaseModel()
        bm.id = "6789"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '6789',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_to__dict(self):
        """
        test to contrast
        """
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_arg(self):
        """
        test args
        """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


class TestBaseModel_save(unittest.TestCase):
    """
    test save model
    """
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_arg(self):
        """
        test save
        """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates(self):
        """
        test save updates
        """
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == "__main__":
    unittest.main()
