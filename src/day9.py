def local_minimum(grid):
    """
    Used for day1
    :param grid: list of list of numbers
    :return: list of local minimums
    """
    lm = []
    for gi, l in enumerate(grid):
        for i, n in enumerate(l):
            if (i == 0) or l[i - 1] > n:
                if (i == len(l) - 1) or l[i + 1] > n:
                    if gi == 0 or grid[gi - 1][i] > n:
                        if gi == len(grid) - 1 or grid[gi + 1][i] > n:
                            lm.append(n + 1)
    return lm


def search_basin(grid, x, y, basin_size, set_of_reached):
    if (x, y) in set_of_reached:
        return
    else:
        set_of_reached.add((x, y))
    if x == 0 or grid[y][x - 1] == 9 or grid[y][x - 1] < grid[y][x]:
        set_of_reached.add((x, y))
    else:  # if grid[y][x - 1] > grid[y][x]:
        search_basin(grid, x - 1, y, basin_size, set_of_reached)
    if (x == len(grid[y]) - 1) or (grid[y][x + 1] == 9) or grid[y][x + 1] < grid[y][x]:
        set_of_reached.add((x, y))
    else:  # if grid[y][x + 1] > grid[y][x]:
        search_basin(grid, x + 1, y, basin_size, set_of_reached)
    if y == 0 or grid[y - 1][x] == 9 or grid[y - 1][x] < grid[y][x]:
        set_of_reached.add((x, y))
    else:  # if grid[y - 1][x] > grid[y][x]:
        search_basin(grid, x, y - 1, basin_size, set_of_reached)
    if (y == len(grid) - 1) or (grid[y + 1][x] == 9) or grid[y + 1][x] < grid[y][x]:
        set_of_reached.add((x, y))
    else:  # if grid[y + 1][x] > grid[y][x]:
        search_basin(grid, x, y + 1, basin_size, set_of_reached)
    return set_of_reached


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
                            basins.append(search_basin(grid, i, gi, 0, set()))
    return basins


if __name__ == '__main__':

    with open("../input/input_day9.txt", "r") as file:
        lines = file.read().splitlines()

    grid = []
    for line in lines:
        grid.append(list(map(int, line)))

    # Answer 1
    print(f"Answer to question 1 = {sum(local_minimum(grid))}")

    # Answer 2
    sorted_list = sorted(basin(grid), key=len)
    print(f"Answer to question 1 = {len(sorted_list[-1]) * len(sorted_list[-2]) * len(sorted_list[-3])} ")
