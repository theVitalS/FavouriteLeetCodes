from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_values = defaultdict(set)
        dict_rows = defaultdict(set)
        dict_columns = defaultdict(set)
        for ir, row in enumerate(board):
            for ic, cell in enumerate(row):
                if cell != ".":
                    if ir in dict_rows[cell]:
                        return False
                    else:
                        dict_rows[cell].add(ir)

                    if ic in dict_columns[cell]:
                        return False
                    else:
                        dict_columns[cell].add(ic)

                    if cell in dict_values[(ir // 3, ic // 3)]:
                        return False
                    else:
                        dict_values[(ir // 3, ic // 3)].add(cell)

        return True


#Second solution bit faster, as we check all conditions and exit without adding to dictionary if False condition is met

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_indexes = defaultdict(set)
        col_indexes = defaultdict(set)
        sqr_indexes = defaultdict(set)

        for y, line in enumerate(board):
            for x, value in enumerate(line):
                if value != '.':
                    if y in row_indexes[value] or x in col_indexes[value]:
                        return False

                    sqr_ind = (y // 3) * 3 + x // 3
                    if sqr_ind in sqr_indexes[value]:
                        return False

                    row_indexes[value].add(y)
                    col_indexes[value].add(x)
                    sqr_indexes[value].add(sqr_ind)

        return True