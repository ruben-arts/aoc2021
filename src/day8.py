def map_to_number(mapping, segments):
    if mapping['a'] in segments and \
            mapping['b'] in segments and \
            mapping['c'] in segments and \
            mapping['d'] in segments and \
            mapping['e'] in segments and \
            mapping['f'] in segments and \
            mapping['g'] in segments:
        return 8
    elif mapping['a'] in segments and \
            mapping['b'] in segments and \
            mapping['c'] in segments and \
            mapping['d'] not in segments and \
            mapping['e'] in segments and \
            mapping['f'] in segments and \
            mapping['g'] in segments:
        return 0
    elif mapping['a'] in segments and \
            mapping['b'] in segments and \
            mapping['c'] not in segments and \
            mapping['d'] in segments and \
            mapping['e'] in segments and \
            mapping['f'] in segments and \
            mapping['g'] in segments:
        return 6
    elif mapping['a'] in segments and \
            mapping['b'] in segments and \
            mapping['c'] in segments and \
            mapping['d'] in segments and \
            mapping['e'] not in segments and \
            mapping['f'] in segments and \
            mapping['g'] in segments:
        return 9
    elif mapping['a'] in segments and \
            mapping['b'] not in segments and \
            mapping['c'] in segments and \
            mapping['d'] in segments and \
            mapping['e'] in segments and \
            mapping['f'] not in segments and \
            mapping['g'] in segments:
        return 2
    elif mapping['a'] in segments and \
            mapping['b'] not in segments and \
            mapping['c'] in segments and \
            mapping['d'] in segments and \
            mapping['e'] not in segments and \
            mapping['f'] in segments and \
            mapping['g'] in segments:
        return 3
    elif mapping['a'] in segments and \
            mapping['b'] in segments and \
            mapping['c'] not in segments and \
            mapping['d'] in segments and \
            mapping['e'] not in segments and \
            mapping['f'] in segments and \
            mapping['g'] in segments:
        return 5
    elif mapping['a'] not in segments and \
            mapping['b'] in segments and \
            mapping['c'] in segments and \
            mapping['d'] in segments and \
            mapping['e'] not in segments and \
            mapping['f'] in segments and \
            mapping['g'] not in segments:
        return 4
    elif mapping['a'] in segments and \
            mapping['b'] not in segments and \
            mapping['c'] in segments and \
            mapping['d'] not in segments and \
            mapping['e'] not in segments and \
            mapping['f'] in segments and \
            mapping['g'] not in segments:
        return 7

    elif mapping['a'] not in segments and \
            mapping['b'] not in segments and \
            mapping['c'] in segments and \
            mapping['d'] not in segments and \
            mapping['e'] not in segments and \
            mapping['f'] in segments and \
            mapping['g'] not in segments:
        return 1


def test_mapping():
    mapy = {'c': 'c', 'f': 'f', 'a': 'a', 'd': 'd', 'b': 'b', 'g': 'g', 'e': 'e'}
    assert map_to_number(mapy, "abcefg") == 0
    assert map_to_number(mapy, "cf") == 1
    assert map_to_number(mapy, "acdeg") == 2
    assert map_to_number(mapy, "acdfg") == 3
    assert map_to_number(mapy, "bcdf") == 4
    assert map_to_number(mapy, "abdfg") == 5
    assert map_to_number(mapy, "abdefg") == 6
    assert map_to_number(mapy, "acf") == 7
    assert map_to_number(mapy, "abcdefg") == 8
    assert map_to_number(mapy, "abcdfg") == 9


def figure_out_mapping(input_string):
    input_d = [d for d in input_string.split()]
    input_d = sorted(input_d, key=lambda d: len(d))
    abc = set("abcdefg")
    connection_map = {}
    # Get the c or f in the display
    connection_map['c'] = input_d[0]
    connection_map['f'] = input_d[0]

    # Get the a in the display
    connection_map['a'] = "".join(set(input_d[1]) - set(connection_map['c']))

    # Get the b or d in the display
    all_others = set(connection_map['a'] + connection_map['c'])
    connection_map['d'] = "".join(set(input_d[2]) - all_others)
    connection_map['b'] = "".join(set(input_d[2]) - all_others)

    # Get the g and e in the display
    for inp in input_d[3:]:
        inps = set(inp)
        if len(inp) == 6:
            all_others = set(connection_map['a'] + connection_map['c'] + connection_map['d'])
            if len(inps - all_others) == 1:
                connection_map['g'] = "".join(inps - all_others)
                connection_map['e'] = "".join(abc - inps)
                break

    # Get the b and din the display
    adg = set("abcdefg")
    for inp in input_d[3:]:
        inps = set(inp)
        if len(inp) == 5:
            adg = adg.intersection(inps)
    connection_map['d'] = "".join(adg - set(connection_map['a']) - set(connection_map['g']))
    connection_map['b'] = "".join(set(connection_map['b']) - set(connection_map['d']))

    # Get the cf in the display
    for inp in input_d[3:]:
        inps = set(inp)
        if len(inp) == 5:
            if connection_map['b'] not in inps and connection_map['e'] in inps:
                connection_map['c'] = "".join(set(connection_map['c']).intersection(inps))
                connection_map['f'] = "".join(set(connection_map['f']) - set(connection_map['c']))
                break
    return connection_map


def test_make_mapping():
    i = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
    assert figure_out_mapping(i) == {'a': 'd', 'b': 'e', 'c': 'a', 'd': 'f', 'e': 'g', 'f': 'b', 'g': 'c'}


if __name__ == '__main__':
    test_make_mapping()
    test_mapping()

    with open("../input/input_day8.txt", "r") as file:
        lines = file.read().splitlines()

    # Parse input
    inputs, outputs = [], []
    for line in lines:
        a = line.split(" | ")
        inputs.append(a[0])
        outputs.append(a[1])

    # Answer question one:
    count = 0
    for output in outputs:
        digits = [d for d in output.split(" ")]
        for d in digits:
            ld = len(d)
            if ld == 2 or ld == 4 or ld == 3 or ld == 7:
                count += 1
    assert count == 397
    print(f"Question one = {count}")

    # Answer question one:
    sum_of_nums = 0
    for index, val in enumerate(inputs):
        mapping = figure_out_mapping(val)
        output_number = ""
        for output in outputs[index].split(" "):
            output_number += str(map_to_number(mapping, output))
        sum_of_nums += int(output_number)
    assert sum_of_nums == 1027422
    print(f"Question one = {sum_of_nums}")
