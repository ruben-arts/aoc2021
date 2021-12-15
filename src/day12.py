import copy

end_paths = set()


def small_cave_visited_twice(path):
    smalls = [cave for cave in path if not cave.isupper()]
    # done = any([smalls.count(cave) > 1 for cave in smalls])
    done = len(set([cave for cave in smalls if smalls.count(cave) > 1]))
    return done


def step(g, path, paths):
    # print(len(end_paths))
    a = g[path[-1]]
    # print(a)
    for cave in a:
        if cave == 'end':
            end_paths.add(path)
            # print(path)
        else:
            if cave.isupper() or (cave not in path) or not small_cave_visited_twice(path):
                if "".join(path) in ["".join(p) for p in paths]:
                    current_path = copy.deepcopy(path)
                    current_path = (*current_path, cave)
                    if not small_cave_visited_twice(current_path):
                        paths.add(current_path)

                else:
                    current_path = (*path, cave)
                    if small_cave_visited_twice(current_path):
                        continue
                step(g, current_path, paths)


def main(lines):
    graph = {}
    for line in lines:
        route = line.split("-")
        if route[0] in graph.keys():
            if route[1] != 'start':
                graph[route[0]].append(route[1])
        else:
            if route[1] != 'start':
                graph[route[0]] = [route[1]]
        if route[1] in graph.keys():
            if route[0] != 'start':
                graph[route[1]].append(route[0])
        else:
            if route[0] != 'start':
                graph[route[1]] = [route[0]]
    # graph.pop('end')
    pathies = {('start')}
    step(graph, ('start',), pathies)
    # set_of_paths = set(tuple(path) for path in end_paths if 'end' == path[-1])
    print(len(end_paths))


if __name__ == '__main__':
    with open("../input/input_day12_test.txt", "r") as file:
        lines = file.read().splitlines()

    main(lines)
