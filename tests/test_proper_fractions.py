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
        self.largeCases = [(9999999, 6637344),
                           (500000003, 500000002)]

    def run_cases(self, cases):
        """Execute the given cases"""
        for inp, expected in cases:
            with self.subTest(num=inp):
                actual = proper_fractions(inp)
                self.assertEqual(actual, expected)

    def test_examples_from_kata(self):
        """Run the test cases from the kata"""
        self.run_cases(self.kataCases)
    
    def test_large_number(self):
        """Run the large number cases"""
        self.run_cases(self.largeCases)
