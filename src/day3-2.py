import copy


def find_common(values, most_common, bit):
    suma = 0
    for value in values:
        line_bit = value[bit]
        if line_bit == '1':
            suma += 1
        else:
            suma -= 1
    if suma == 0:
        return most_common
    else:
        return most_common == (suma > 0)


def remove_when_bit(index, value_that_lives, values):
    new_values = []
    for value in values:
        if value[index] == value_that_lives:
            new_values.append(value)
    return new_values


def find_rating(most_common):
    deep_copy = copy.deepcopy(plain_file)
    for bit in range(0, len(plain_file[0])):
        if len(deep_copy) > 1:
            common_is_positive = find_common(deep_copy, most_common, bit)
            deep_copy = remove_when_bit(bit, '1' if common_is_positive else '0', deep_copy)
    return int(deep_copy[0], 2)


if __name__ == '__main__':
    with open("../input/input_day3.txt", "r") as file:
        plain_file = file.read().splitlines()

    ox = find_rating(True)
    co2 = find_rating(False)
    print(f" Oxygen generator rating = {ox}")
    print(f" CO2 generator rating = {co2}")
    print(f" Life support rating = {ox*co2}")
