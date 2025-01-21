class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        s0 = sum(grid[0])
        s1 = 0

        r = float('inf')
        for i in range(len(grid[0])):
            s0 -= grid[0][i]
            s1 += grid[1][i]
            if s1 >= s0:
                return max(s1-grid[1][i], s0)