import copy


def check_horz(grid, number):
    bingo = False
    for line in grid:
        for i in range(len(line)):
            if line[i] == number:
                line[i] = '*'
        bingo = all([x == '*' for x in line])
        if bingo:
            return bingo
    return False


def check_vert(grid, number):
    bingo = False
    for index in range(0, 5):
        vert_line = []
        for line in grid:

            if line[index] == number:
                line[index] = '*'
            vert_line.append(line[index])
        bingo = all([x == '*' for x in vert_line])
        if bingo:
            return bingo
    return bingo


def sum_grid(grid):
    suma = 0
    for line in grid:
        for x in line:
            if x != '*':
                suma += int(x)
    return suma


if __name__ == '__main__':
    with open("../input/input_day4.txt", "r") as file:
        plain_file = file.read().splitlines()

    called_numbers = plain_file.pop(0).split(",")
    list_of_grids = [[]]

    # Gridify
    for line in plain_file:
        if line == "":
            list_of_grids.append([])
        else:
            list_of_grids[-1].append(line.rsplit())

    for number in called_numbers:
        list_of_grids_to_remove = []
        for grid in list_of_grids:
            bingo = False
            bingo = check_vert(grid, number)
            bingo = check_horz(grid, number) or bingo

            if bingo:
                sum_of_grid = sum_grid(grid)
                print(f"answer to the fist question = {sum_of_grid * int(number)} sum of grid was {sum_of_grid} and the number was {number}")
                list_of_grids_to_remove.append(grid)

        for grid in  list_of_grids_to_remove:
            if len(list_of_grids) > 1:
                list_of_grids.remove(grid)
            else:
                sum_of_grid = sum_grid(list_of_grids[0])
                print(sum_of_grid * int(number))
                exit(0)
