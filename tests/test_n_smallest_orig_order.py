"""Tests for the n_smallest_orig_order kata"""

import unittest

from solutions.n_smallest_orig_order import first_n_smallest, performant_smallest


class NSmallestOrigOrderTest(unittest.TestCase):
    """N-smallest orig order test suite"""

    def setUp(self):
        """Initialize the methods to call"""
        self._methods = [
            first_n_smallest,
            performant_smallest
        ]

    def execute_test(self, inputArr, inputCount, expected):
        """Run the tests for both methods."""
        for method in self._methods:
            with self.subTest(case=method.__name__):
                actual = method(inputArr, inputCount)
                self.assertEqual(actual, expected)

    def test_simple_case(self):
        inputArr = [1, 2, 3, 4, 5]
        inputCount = 3
        expected = [1, 2, 3]
        self.execute_test(inputArr, inputCount, expected)
