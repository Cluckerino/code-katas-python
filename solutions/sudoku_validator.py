"""
Validate the given sudoku solution.
https://www.codewars.com/kata/sudoku-solution-validator/python
"""


def validSolution(board):
    """Check if the given board is a valid sudoku solution. Expects an input as a list of rows."""
    pass


def get_box_num(col_num, row_num):
    """Get the box number given the column and row."""
    return 3 * int(row_num/3) + int(col_num/3)
