from collections import deque

class Solution:
    def get_neighbours(self, y, x):
        neighbours = []

        if y > 0: neighbours.append((y-1, x))
        if y < self.m - 1: neighbours.append((y+1, x))
        if x > 0: neighbours.append((y, x-1))
        if x < self.n - 1: neighbours.append((y, x+1))

        return neighbours

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.m = len(grid)     #hight, y max
        self.n = len(grid[0])  #width, x max
        obstacles = [[float('inf') for _ in range(self.n)] for _ in range(self.m)]

        c = [(0, 0)]
        d = deque(c)
        checked = set(c)

        if grid[0][0] == 0: obstacles[0][0] =  0
        else: obstacles[0][0] = 1


        while d:
            y, x = d.popleft()
            obs_count = obstacles[y][x]

            for n in self.get_neighbours(y, x):
                if n not in checked:
                    checked.add(n)

                    yn = n[0]
                    xn = n[1]
                    v = grid[yn][xn]
                    obs_count = obstacles[y][x]

                    if yn == self.m - 1 and xn == self.n - 1:
                        return obs_count+v

                    if v == 0: d.appendleft((yn, xn))
                    else: d.append((yn, xn))

                    obstacles[yn][xn] = obs_count+v


        print('end reached')
        return obstacles[self.m-1][self.n-1]