# Not the most efficient solution (beats only 50%), but I really enjoined creating it.

def discover_island(grid, coordinates, to_check):
    neighbours = get_neighbours(coordinates, to_check)

    while neighbours:
        cell = neighbours.pop()
        to_check.remove(cell)
        neighbours.update(get_neighbours(cell, to_check))


def get_neighbours(coordinates, to_check):
    res = set()
    y = coordinates[0]
    x = coordinates[1]

    if (y - 1, x) in to_check: res.add((y - 1, x))
    if (y + 1, x) in to_check: res.add((y + 1, x))
    if (y, x - 1) in to_check: res.add((y, x - 1))
    if (y, x + 1) in to_check: res.add((y, x + 1))

    return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        to_check = set()
        result = 0

        for y, line in enumerate(grid):
            for x, value in enumerate(line):
                if grid[y][x] == "1": to_check.add((y, x))

        while to_check:
            cell = to_check.pop()
            result += 1
            discover_island(grid, cell, to_check)

        return result