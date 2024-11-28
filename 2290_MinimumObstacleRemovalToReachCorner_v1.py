from collections import deque

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)  # height, y max
        n = len(grid[0])  # width, x max
        # number of obstacles to be removed to reach point, -1 represents cell being not checked yet
        obstacles = [[-1 for _ in range(n)] for _ in range(m)]

        # initialize 'start' cell
        c = [(0, 0)]
        d = deque(c)  # deque of cells to be checked
        obstacles[0][0] = grid[0][0]

        while d:
            y, x = d.popleft()
            obs_count = obstacles[y][x]

            neighbours = []

            # adding only not checked columns which do not brake borders 
            if y > 0 and obstacles[y - 1][x] == -1: neighbours.append((y - 1, x))
            if y < m - 1 and obstacles[y + 1][x] == -1: neighbours.append((y + 1, x))
            if x > 0 and obstacles[y][x - 1] == -1: neighbours.append((y, x - 1))
            if x < n - 1 and obstacles[y][x + 1] == -1: neighbours.append((y, x + 1))

            for yn, xn in neighbours:
                v = grid[yn][xn]

                if yn == m - 1 and xn == n - 1:
                    return obs_count + v

                # if cell is empy add to beginning of deque, if not - to the end
                # we want to check empty cells first
                if v == 0:
                    d.appendleft((yn, xn))
                else:
                    d.append((yn, xn))

                obstacles[yn][xn] = obs_count + v
