"""Tests for the fold_an_array kata"""

import unittest

from solutions.fold_an_array import fold_array


class FoldAnArrayTest(unittest.TestCase):
    """Fold-an-array test suite"""

    def test_fold_array_single_run(self):
        """Test fold function for a single fold"""
        self.assertEqual(fold_array([1, 2, 3, 4, 5], 1), [6, 6, 3])

    def test_fold_array_multi_run(self):
        """Test fold function for multiple folds"""
        self.assertEqual(fold_array([1, 2, 3, 4, 5], 2), [9, 6])
