import copy


def step(g, path, paths):
    for i, cave in enumerate(g[path[-1]]):
        # print(cave)
        if cave == 'end':
            print(f"END {path.append(cave)}")

        else:
            if cave in path and not cave.isupper():
                continue
            if "".join(path) in ["".join(p) for p in paths]:
                current_path = copy.deepcopy(path)
                current_path.append(cave)
                paths.append(current_path)
            else:
                path.append(cave)
                current_path = path
            step(g, current_path, paths)


def main(lines):
    graph = {}
    for line in lines:
        route = line.split("-")
        if route[0] in graph.keys():
            graph[route[0]].append(route[1])
        else:
            graph[route[0]] = [route[1]]
        if route[1] in graph.keys():
            graph[route[1]].append(route[0])
        else:
            graph[route[1]] = [route[0]]

    pathies = [['start']]
    step(graph, ['start'], pathies)
    set_of_paths = set(tuple(path) for path in pathies if 'end' == path[-1])
    print(len(set_of_paths))


if __name__ == '__main__':
    with open("../input/input_day12.txt", "r") as file:
        lines = file.read().splitlines()

    main(lines)
