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
        """Simple test case"""
        self.execute_test([1, 2, 3, 4, 5], 3, [1, 2, 3])

    def test_reverse(self):
        """Test a reversed array"""
        self.execute_test([5, 4, 3, 2, 1], 3, [3, 2, 1])

    def test_repeats(self):
        """Test an array with repeated values"""
        self.execute_test([1, 2, 3, 1, 2], 3, [1, 2, 1])

    def test_negative(self):
        """Test an array with negaive values"""
        self.execute_test([1, 2, 3, -4, 0], 3, [1, -4, 0])

    def test_take_0(self):
        """Test returning an empty array if taking 0"""
        self.execute_test([1, 2, 3, 4, 5], 0, [])

    def test_take_all(self):
        """Test taking all values"""
        self.execute_test([1, 2, 3, 4, 2], 5, [1, 2, 3, 4, 2])

    def test_take_all_but_1(self):
        """Test taking all but 1 values"""
        self.execute_test([1, 2, 3, 4, 2], 4, [1, 2, 3, 2])

    def test_aggressive_repeats(self):
        """Test with more aggressive repeats"""
        inputArr = [2, 1, 2, 3, 4, 2]
        expecteds = {
            2: [2, 1],
            3: [2, 1, 2],
            4: [2, 1, 2, 2],
            5: [2, 1, 2, 3, 2],
        }
        for inputCount, expected in expecteds.items():
            with self.subTest(taking=inputCount):
                self.execute_test(inputArr, inputCount, expected)
