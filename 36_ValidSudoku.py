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