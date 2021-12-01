# Puzzle 1 of day 1
# https://adventofcode.com/2021/day/1

last_value = 0
larger = -1
with open("../input/input_day1-1.txt", "r") as file:
    for line in file:
        if int(line) > last_value:
            larger += 1
        last_value = int(line)
print(f"{larger} measurements are larger then the one before it. ")

# Answer for this puzzle with this input was: 1466
