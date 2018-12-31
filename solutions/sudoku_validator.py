"""
Validate the given sudoku solution.
https://www.codewars.com/kata/sudoku-solution-validator/python
"""


def validSolution(board):
    """Check if the given board is a valid sudoku solution. Expects an input as a list of rows."""
    # Create sets with expected values
    rows = [set(range(1, 10)) for _ in range(0, 9)]
    cols = [set(range(1, 10)) for _ in range(0, 9)]
    # Yes, it's misspelled
    boxs = [set(range(1, 10)) for _ in range(0, 9)]
    try:
        for r in range(0, 9):
            for c in range(0, 9):
                b = get_box_num(c, r)
                val = board[r][c]
                # Validate value
                if val > 9 or val < 1:
                    return False
                # To validate row/col/box, remove a value from the corresponding set.
                # Will throw exception if invalid.
                rows[r].remove(val)
                cols[c].remove(val)
                boxs[b].remove(val)
    except KeyError:
        return False
    return True


def get_box_num(col_num, row_num):
    """Get the box number given the column and row."""
    return 3 * int(row_num/3) + int(col_num/3)
