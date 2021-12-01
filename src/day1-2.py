# Puzzle 2 of day 1
# https://adventofcode.com/2021/day/1

last_value = 0
larger = -1
with open("input/input_day1-1.txt", "r") as file:
    plain_file = file.readlines()

for index, value in enumerate(plain_file):
    if len(plain_file) > index + 2:
        current_sum = int(plain_file[index]) + int(plain_file[index + 1]) + int(plain_file[index + 2])
        if current_sum > last_value:
            larger += 1
        last_value = current_sum
print(f"{larger} measurements are larger then the one before it. ")

# Answer for this puzzle with this input was: 1491
