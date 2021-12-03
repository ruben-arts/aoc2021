with open("../input/input_day3.txt", "r") as file:
    plain_file = file.readlines()

first_line = plain_file[0]
len_first_line = len(first_line)
gamma = 0
epsilon = 0
suma = 0
for bit in range(len_first_line-2, -1, -1):
    for line in plain_file:
        line_bit = line[len_first_line-2-bit]
        if line_bit == '0':
            suma += 1
        else:
            suma -= 1
    print(suma)
    print(f"bit = {bit}")
    if suma > 0:
        gamma += 2 ** bit
    suma = 0
print(f"gamma rate: {gamma}")
epsilon = gamma ^ 0b111111111111
print(f"epsilon rate: {epsilon}")
print(f"gamma rate: {bin(gamma)}")
print(f"epsilon rate: {bin(epsilon)}")
print(f"gamma * epsilon = powerconsumption = {gamma*epsilon}")