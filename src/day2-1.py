with open("../input/input_day2-1.txt", "r") as file:
    plain_file = file.readlines()

x, y, aim = 0, 0, 0
for line in plain_file:
    direction, distance = line.split()
    if direction == "forward":
        x += int(distance)
        y += int(distance) * aim
    elif direction == "down":
        aim += int(distance)
    elif direction == "up":
        aim -= int(distance)

print(x)
print(y)
print(f"depth = {y} and location x = {x} and aim = {aim}")
print(f"multiplied x * y is : {x*y}")