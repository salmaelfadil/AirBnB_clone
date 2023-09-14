#!/usr/bin/python3
"""
review model tests
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
        """testing Review Class"""

        def test_review(self):
            """
            test review class
            """
            self.assertEqual(Review.place_id, "")
            self.assertEqual(Review.user_id, "")
            self.assertEqual(Review.text, "")
            self.assertTrue(issubclass(Review, Review))

        def test_review(self):
            """
            test instance
            """
            review = Review()
            self.assertTrue(isinstance(review, Review))


if __name__ == "__main__":
    unittest.main()
