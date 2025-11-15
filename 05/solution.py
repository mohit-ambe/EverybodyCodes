files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

quality = lambda spine:"".join(str(p) for p, l, r in spine)
levels = lambda spine:[int(str(l) + str(p) + str(r)) for p, l, r in spine]


def build_spine(nodes):
    spine = []
    for node in nodes:
        added = False
        for s in range(len(spine)):
            parent, l, r = spine[s]
            if node < parent and l == "":
                spine[s][1] = node
                added = True
                break
            if node > parent and r == "":
                spine[s][2] = node
                added = True
                break
        if not added:
            spine.append([node, "", ""])
    return spine


def part1(data=dataset[0]):
    id, nodes = data[0].split(":")
    nodes = list(map(int, nodes.split(",")))
    spine = build_spine(nodes)
    print(quality(spine))


def part2(data=dataset[1]):
    qualities = []
    for line in data:
        id, nodes = line.split(":")
        nodes = list(map(int, nodes.split(",")))
        spine = build_spine(nodes)
        qualities.append(int(quality(spine)))
    print(max(qualities) - min(qualities))


def part3(data=dataset[2]):
    ranks = []
    for line in data:
        id, nodes = line.split(":")
        nodes = list(map(int, nodes.split(",")))
        spine = build_spine(nodes)
        # sort each sword on [quality, level 1, level 2, ... last level, id]
        r = [int(quality(spine))] + levels(spine) + [int(id)]
        ranks.append(r)
        ranks.sort(reverse=True)
    print(sum([(i + 1) * r[-1] for i, r in enumerate(ranks)]))


part1()
part2()
part3()
