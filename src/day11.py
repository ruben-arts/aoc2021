def get_coords_neighbor(x, y, grid_len):
    # def in_grid(val):
    #     if val < 0 or val > grid_len:
    #         return False
    #     else:
    #         return True

    return {(max(x - 1, 0), max(y - 1, 0)), (x, max(y - 1, 0)), (min(x + 1, grid_len), max(y - 1, 0)),
            (min(x + 1, grid_len), y), (min(x + 1, grid_len), min(y + 1, grid_len)), (x, min(y + 1, grid_len)),
            (max(x - 1, 0), min(y + 1, grid_len)), (max(x - 1, 0), y)}


def flash_octo(grid, x, y, set_of_flashed):
    flashes = 0
    if grid[y][x] > 9 and (x, y) not in set_of_flashed:
        set_of_flashed.add((x, y))
        flashes += 1
        grid[y][x] = 0
        for neighbor in get_coords_neighbor(x, y, len(grid) - 1):
            if neighbor not in set_of_flashed:
                grid[neighbor[1]][neighbor[0]] += 1
                flashes += flash_octo(grid, neighbor[0], neighbor[1], set_of_flashed)
    return flashes


def main(grid):
    flashes = 0
    for step in range(1000):
        # Step one, add one to all octos
        for yi, y in enumerate(grid):
            for xi, octo in enumerate(y):
                grid[yi][xi] += 1

        # Step two, flash all octos above 9 and neighbors
        set_of_flashed = set()
        for yi, y in enumerate(grid):
            for xi, octo in enumerate(y):
                flashes += flash_octo(grid, xi, yi, set_of_flashed)

        if grid == [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]:
            print(f"grid just flashed completely at step {step}")
    print(f"amount of flashes = {flashes}")


if __name__ == '__main__':

    with open("../input/input_day11.txt", "r") as file:
        lines = file.read().splitlines()
    grid = []
    for line in lines:
        grid.append(list(map(int, list(line))))

    main(grid)
