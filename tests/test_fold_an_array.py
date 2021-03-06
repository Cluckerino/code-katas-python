"""Tests for the fold_an_array kata"""

import unittest

from solutions.fold_an_array import fold_array, fold_array_once


class FoldAnArrayTest(unittest.TestCase):
    """Fold-an-array test suite"""

    def test_fold_array_once(self):
        """Test the single fold fuunction"""
        # cases = input, expected
        cases = [
            ([1, 2, 3, 4, 5], [6, 6, 3]),
            ([6, 6, 3], [9, 6])
        ]
        for inp, exp in cases:
            with self.subTest(inp=inp):
                self.assertEqual(fold_array_once(inp), exp)

    def test_fold_array_single_run(self):
        """Test fold function for a single fold"""
        self.assertEqual(fold_array([1, 2, 3, 4, 5], 1), [6, 6, 3])

    def test_fold_array_multi_run(self):
        """Test fold function for multiple folds"""
        self.assertEqual(fold_array([1, 2, 3, 4, 5], 2), [9, 6])
