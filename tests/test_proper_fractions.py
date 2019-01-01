"""Tests for the proper fractions kata"""

import unittest

from solutions.proper_fractions import proper_fractions


class ProperFractionsTest(unittest.TestCase):
    """Proper fractions test suite"""

    def setUp(self):
        """Set up test cases from kata"""
        self.kataCases = [(1, 0),
                          (2, 1),
                          (5, 4),
                          (15, 8),
                          (25, 20)]

    def test_examples_from_kata(self):
        """Run the test cases from the kata"""
        for inp, expected in self.kataCases:
            with self.subTest(num=inp):
                actual = proper_fractions(inp)
                self.assertEqual(actual, expected)
