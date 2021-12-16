import copy


def input_to_amount_of_pairs(startinglist):
    map_amount_of_pairs = {}
    for i, elm in enumerate(startinglist):
        if i + 1 < len(startinglist):
            pair = elm + startinglist[i + 1]
            if pair in map_amount_of_pairs.keys():
                map_amount_of_pairs[pair] += 1
            else:
                map_amount_of_pairs[pair] = 1
    return map_amount_of_pairs


if __name__ == '__main__':
    with open("../input/input_day14.txt", "r") as file:
        lines = file.read().splitlines()

    start = lines[0]

    insertions = lines[2:]

    commands = {}

    map_amount_of_pairs = input_to_amount_of_pairs(start)

    map_pair_to_new_pairs = {}
    for i in insertions:
        pair, insertable = i.split(" -> ")
        map_pair_to_new_pairs[pair] = [pair[0] + insertable, insertable + pair[1]]

    for _ in range(40):
        cp_map_amount_of_pairs = copy.deepcopy(map_amount_of_pairs)
        for pair in cp_map_amount_of_pairs:
            if pair in map_pair_to_new_pairs and cp_map_amount_of_pairs[pair] > 0:
                a, b = map_pair_to_new_pairs[pair]
                growth = cp_map_amount_of_pairs[pair]
                cp_map_amount_of_pairs[pair] = 0
                map_amount_of_pairs[pair] -= growth
                if a in map_amount_of_pairs.keys():
                    map_amount_of_pairs[a] += growth
                else:
                    map_amount_of_pairs[a] = growth
                if b in map_amount_of_pairs.keys():
                    map_amount_of_pairs[b] += growth
                else:
                    map_amount_of_pairs[b] = growth

    count_letters = {}
    for pair in map_amount_of_pairs:
        a = pair[0]
        b = pair[1]
        if a in count_letters.keys():
            count_letters[a] += map_amount_of_pairs[pair]
        else:
            count_letters[a] = map_amount_of_pairs[pair]
        if b in count_letters.keys():
            count_letters[b] += map_amount_of_pairs[pair]
        else:
            count_letters[b] = map_amount_of_pairs[pair]

    # Count edges because they will not have a pair with the ends
    count_letters[start[0]] += 1
    count_letters[start[-1]] += 1

    # Divide because the pairs are double
    for letter in count_letters:
        count_letters[letter] = count_letters[letter]/2

    print(f"max - min = {max(count_letters.values()) - min(count_letters.values())}")
