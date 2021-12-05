import re


def add_coord_to_set(coord, overlap, coords):
    if coord in coord_set:
        overlap.add(coord)
    else:
        coords.add(coord)


if __name__ == '__main__':
    with open("../input/input_day5.txt", "r") as file:
        plain_file = file.read()

    # Listify
    list_of_lines_endpoints = []
    regex = r"(\d*),(\d*) -> (\d*),(\d*)"
    matches = re.findall(regex, plain_file, re.MULTILINE)
    for match in matches:
        int_match = tuple(map(int, match))
        # Check for horizontal or vertical lines:
        if int_match[0] == int_match[2] or int_match[1] == int_match[3]:
            list_of_lines_endpoints.append(int_match)
        # Check for diagonals COMMENT FOR ANSWER 1:
        elif abs(int_match[0] - int_match[2]) == abs(int_match[1] - int_match[3]):
            list_of_lines_endpoints.append(int_match)

    # Put all coordinates in list
    coord_list = []
    coord_set = set()
    overlapping_coord_set = set()
    for line in list_of_lines_endpoints:
        if line[0] == line[2]:
            for y in range(line[1], line[3], -1 if line[1] > line[3] else 1):
                coord = (line[0], y)
                add_coord_to_set(coord, overlapping_coord_set, coord_set)
            add_coord_to_set((line[2], line[3]), overlapping_coord_set, coord_set)
        elif line[1] == line[3]:
            for x in range(line[0], line[2], -1 if line[0] > line[2] else 1):
                coord = (x, line[1])
                add_coord_to_set(coord, overlapping_coord_set, coord_set)
            add_coord_to_set((line[2], line[3]), overlapping_coord_set, coord_set)
        else:
            y = line[1]
            x_direction = -1 if line[0] > line[2] else 1
            y_direction = -1 if line[1] > line[3] else 1
            for x in range(line[0], line[2], x_direction):
                coord = (x,y)
                add_coord_to_set(coord, overlapping_coord_set, coord_set)
                y = y + y_direction
            add_coord_to_set((line[2], line[3]), overlapping_coord_set, coord_set)
    print(f"lenght of overlapping = {len(overlapping_coord_set)}")
