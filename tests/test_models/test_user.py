#!/usr/bin/python3
"""
test user model
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class Test_user(unittest.TestCase):
    """Tests the user module"""
    def test_class(self):
        """
        test class
        """
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertTrue(issubclass(User, BaseModel))

    def test_str_repr(self):
        """
        testing str representation
        """
        user = User()
        cls = user.__class__.__name__
        id_ = user.id
        str_format = "[{}] ({}) {}".format(cls, id_, user.__dict__)
        self.assertEqual(user.__str__(), str_format)

    def test_instance(self):
        """
        test all the instance
        """
        user = User()
        self.assertTrue(isinstance(user, BaseModel))
        self.assertIsInstance(user, User)

    def test_save(self):
        """
        test save operation and check updated_at attr
        """
        user = User()
        old_save = user.updated_at
        user.save()
        new_save = user.updated_at
        self.assertNotEqual(old_save, new_save)


if __name__ == "__main__":
    unittest.main()
