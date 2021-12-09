import sys


def local_minimum(grid):
    lm = []
    for gi, l in enumerate(grid):
        for i, n in enumerate(l):
            if (i == 0) or l[i - 1] > n:
                if (i == len(l) - 1) or l[i + 1] > n:
                    if gi == 0 or grid[gi - 1][i] > n:
                        if gi == len(grid) - 1 or grid[gi + 1][i] > n:
                            lm.append(n + 1)
    return lm


def search_basin(grid, x, y, basin_size):
    if x == 0 or grid[y][x - 1] == 9:
        basin_size += 1
    else:
        search_basin(grid, x - 1, y, basin_size)
    if (x == len(grid[y]) - 1) or (grid[y][x + 1] == 9):
        basin_size += 1
    else:
        search_basin(grid, x + 1, y, basin_size)
    if y == 0 or grid[y - 1][x] == 9:
        basin_size += 1
    else:
        search_basin(grid, x, y - 1, basin_size)
    if y == len(grid) - 1 or grid[y + 1][x] == 9:
        basin_size += 1
    else:
        search_basin(grid, x, y + 1, basin_size)
    return basin_size


def basin(grid):
    basins = []
    # find local minima
    for gi, l in enumerate(grid):
        for i, n in enumerate(l):
            if (i == 0) or l[i - 1] > n:
                if (i == len(l) - 1) or l[i + 1] > n:
                    if gi == 0 or grid[gi - 1][i] > n:
                        if gi == len(grid) - 1 or grid[gi + 1][i] > n:
                            # Local minima found, check basin size:
                            return search_basin(grid, i, gi, 0)


if __name__ == '__main__':

    list_of_heights = []
    with open("../input/input_day9_test.txt", "r") as file:
        lines = file.read().splitlines()
    grid = []
    for line in lines:
        grid.append(list(map(int, line)))
    print(grid)
    print(f"Answer to question 1 = {sum(local_minimum(grid))}")
    sys.setrecursionlimit(1500)
    print(basin(grid))
