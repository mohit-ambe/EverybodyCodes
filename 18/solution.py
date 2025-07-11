from heapq import heappop, heappush

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def water_farm(data, sources, reverse=False):
    farm = {(y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] != "#"}
    destination = ("P" if not reverse else ".")
    targets = {(y, x) for (y, x) in farm if data[y][x] == destination}

    targets_reached = dict()
    Q = [(0, source) for source in sources]
    visited = set()

    while Q:
        d, (y, x) = heappop(Q)

        if data[y][x] == destination and (y, x) not in targets_reached:
            targets_reached[(y, x)] = d

        if targets_reached.keys() == targets:
            return d if not reverse else targets_reached

        if (y, x) in visited:
            continue
        visited.add((y, x))

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            np = (y + dy, x + dx)
            if np in farm:
                heappush(Q, (d + 1, np))

    return -1 if not reverse else dict()


def part1(data=dataset[0]):
    print(water_farm(data, [(1, 0)]))


def part2(data=dataset[1]):
    print(water_farm(data, [(1, 0), (len(data) - 2, len(data[0]) - 1)]))


def part3(data=dataset[2]):
    # reverse search: find paths from palm trees to wells,
    # sum distances and return minimum
    palm_trees = {(y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "P"}
    wells = dict()
    for i, palm in enumerate(palm_trees):
        for loc, dist in water_farm(data, [palm], reverse=True).items():
            wells[loc] = wells.get(loc, 0) + dist
    print(min(wells.values()))


part1()
part2()
part3()
