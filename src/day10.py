def has_illegals(line):
    closing_chars = {']', '}', ')', '>'}
    map_c = {']': '[', ')': '(', '}': '{', '>': '<'}
    opens = []
    for char in line:
        if char in closing_chars:
            popped = opens.pop(-1)
            if map_c[char] != popped:
                return char
                break

        else:
            opens.append(char)


def find_remainings(line):
    closing_chars = {']', '}', ')', '>'}
    map_c = {'[': ']', '(': ')', '{': '}', '<': '>'}
    opens = []
    for char in line:
        if char in closing_chars:
            opens.pop(-1)
        else:
            opens.append(char)
    return [map_c[c] for c in opens]


if __name__ == '__main__':

    with open("../input/input_day10.txt", "r") as file:
        lines = file.read().splitlines()
    ll = []
    for line in lines:
        ll.append(list(line))

    illegals = []
    remainings = []
    for line in lines:
        ill = has_illegals(line)
        if ill:
            illegals.append(ill)
        else:
            remainings.append(find_remainings(line)[::-1])

    error = 0
    for i in illegals:
        if i == ')':
            error += 3
        if i == ']':
            error += 57
        if i == '}':
            error += 1197
        if i == '>':
            error += 25137
    print(f"anwser part 1 = {error}")

    score_map = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for i in remainings:
        score = 0
        for char in i:
            score = (score * 5) + score_map[char]
        print(score)
        scores.append(score)
    scores.sort()
    middle = [scores[i] for i in range(int((len(scores) / 2) - (1 if float(len(scores)) % 2 == 0 else 0)), int(len(scores) / 2 + 1))]
    print(f"anwser part 2 = {middle}")
