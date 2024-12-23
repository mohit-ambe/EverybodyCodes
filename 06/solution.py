files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def build_tree(data):
    tree = dict()
    for line in data:
        parent, children = line.split(":")
        children = {c for c in children.split(",")}
        tree[parent] = children
    return tree


def explore(tree):
    powerful = dict()
    Q = [["RR"]]
    while Q:
        path = Q.pop(0)
        key = path[-1]
        if key == "@":
            if len(path) not in powerful:
                powerful[len(path)] = path
            else:
                powerful[len(path)] = None
        if key not in tree:
            continue
        for k in [k for k in tree[key] if key not in tree.get(k, [])]:
            Q.append(path + [k])
    return [v for v in powerful.values() if v][0]


def part1(data=dataset[0]):
    path = explore(build_tree(data))
    print("".join(path))


def part2(data=dataset[1]):
    path = explore(build_tree(data))
    print("".join([p[0] for p in path]))


def part3(data=dataset[2]):
    path = explore(build_tree(data))
    print("".join([p[0] for p in path]))


part1()
part2()
part3()
