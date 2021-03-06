"""Tests for the sudoku validator kata"""

import unittest

from solutions.sudoku_validator import validSolution, get_box_num


class SudokuValidatorTest(unittest.TestCase):
    """Sudoku validator test suite"""

    def setUp(self):
        """Init the examples from the kata."""
        self.good_solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                              [6, 7, 2, 1, 9, 5, 3, 4, 8],
                              [1, 9, 8, 3, 4, 2, 5, 6, 7],
                              [8, 5, 9, 7, 6, 1, 4, 2, 3],
                              [4, 2, 6, 8, 5, 3, 7, 9, 1],
                              [7, 1, 3, 9, 2, 4, 8, 5, 6],
                              [9, 6, 1, 5, 3, 7, 2, 8, 4],
                              [2, 8, 7, 4, 1, 9, 6, 3, 5],
                              [3, 4, 5, 2, 8, 6, 1, 7, 9]]
        self.bad_solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                             [6, 7, 2, 1, 9, 0, 3, 4, 9],
                             [1, 0, 0, 3, 4, 2, 5, 6, 0],
                             [8, 5, 9, 7, 6, 1, 0, 2, 0],
                             [4, 2, 6, 8, 5, 3, 7, 9, 1],
                             [7, 1, 3, 9, 2, 4, 8, 5, 6],
                             [9, 0, 1, 5, 3, 7, 2, 1, 4],
                             [2, 8, 7, 4, 1, 9, 6, 3, 5],
                             [3, 0, 0, 4, 8, 1, 1, 7, 9]]
        self.box_nums = [[0, 0, 0, 1, 1, 1, 2, 2, 2],
                         [0, 0, 0, 1, 1, 1, 2, 2, 2],
                         [0, 0, 0, 1, 1, 1, 2, 2, 2],
                         [3, 3, 3, 4, 4, 4, 5, 5, 5],
                         [3, 3, 3, 4, 4, 4, 5, 5, 5],
                         [3, 3, 3, 4, 4, 4, 5, 5, 5],
                         [6, 6, 6, 7, 7, 7, 8, 8, 8],
                         [6, 6, 6, 7, 7, 7, 8, 8, 8],
                         [6, 6, 6, 7, 7, 7, 8, 8, 8]]

    def test_good_solution(self):
        """Example test from kata"""
        self.assertTrue(validSolution(self.good_solution))

    def test_bad_solution(self):
        """Example test from kata"""
        self.assertFalse(validSolution(self.bad_solution))

    def test_get_box_num(self):
        """Test the box number getter"""
        for r in range(0, 9):
            for c in range(0, 9):
                self.assertEqual(get_box_num(c, r), self.box_nums[r][c])
