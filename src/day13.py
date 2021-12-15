
def print_paper(sheet, height, width):
    for y in sheet[:int(height)]:
        print("".join(y[:int(width)]))
    print()

if __name__ == '__main__':

    with open("../input/input_day13.txt", "r") as file:
        lines = file.read().splitlines()

    coordinates = [tuple(c.split(",")) for c in lines if c and 'fold' not in c]
    folds = [tuple(c.split("=")) for c in lines if 'fold' in c]

    coordinates = [(int(c[0]), int(c[1])) for c in coordinates]
    width = max([c[0] for c in coordinates])
    height = max([c[1] for c in coordinates])

    paper = []
    for y in range(height+1):
        paper.append([])
        for x in range(width+1):
            if (x, y) in coordinates:
                paper[y].append('#')
            else:
                paper[y].append('.')

    remaining_height = 0
    remaining_width = 0
    for fold_number, fold in enumerate(folds):
        foldline = int(fold[1])
        if 'x' in fold[0]:
            remaining_width = foldline
            for row in paper:
                for i, x in enumerate(row):
                    if x == '#' and i > foldline:
                        row[foldline-(i-foldline)] = '#'
                        row[i] = '.'
        if 'y' in fold[0]:
            remaining_height = foldline
            for i, row in enumerate(paper):
                for ix, x in enumerate(row):
                    if x == '#' and i > foldline-1:
                        paper[foldline-(i-foldline)][ix] = '#'
                        paper[i][ix] = '.'
        if fold_number == 0:
            count = 0
            for y in paper:
                count += y.count('#')
            print(f"answer1 = {count}")

    # Asnwer 2
    print_paper(paper, remaining_height, remaining_width)

