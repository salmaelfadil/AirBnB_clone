#!/usr/bin/python3
"""
State model tests
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    test State model
    """
    def test_state_class(self):
        """
        test state class
        """
        self.assertEqual(State.name, "")
        self.assertTrue(State, BaseModel)
        self.assertTrue(issubclass(State, BaseModel))

    def test_all_instances(self):
        """
        test instance
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_save(self):
        """
        testing the save and check updated_at attr
        """
        state = State()
        old_save = state.updated_at
        state.save()
        new_save = state.updated_at
        self.assertNotEqual(old_save, new_save)


if __name__ == "__main__":
    unittest.main()
