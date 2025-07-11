from heapq import heappop, heappush

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def find_constellations(data, p3=False):
    manhattan = lambda y1, x1, y2, x2:abs(y2 - y1) + abs(x2 - x1)
    stars = {(y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "*"}

    size = [0]
    visited = set()
    Q = [(0, (-1, -1), list(stars)[0])]

    while stars - visited:
        if Q:
            w, u, v = heappop(Q)
        else:
            # if the queue is empty, a brilliant constellation was completed
            # restart from a random unvisited point
            w, u, v = (0, (-1, -1), list(stars - visited)[0])
            size.append(0)

        if v in visited:
            continue
        visited.add(v)

        size[-1] += w + 1

        # add adjacent minimum edges until add vertices have been visited,
        # forming the MST for the constellations
        for dv in stars - {v}:
            d = manhattan(*v, *dv)
            if not p3 or (p3 and d < 6):
                heappush(Q, (d, v, dv))

    size.sort()
    return size[-1] * size[-2] * size[-3] if p3 else size[0]


def part1(data=dataset[0]):
    print(find_constellations(data))


def part2(data=dataset[1]):
    print(find_constellations(data))


def part3(data=dataset[2]):
    print(find_constellations(data, p3=True))


part1()
part2()
part3()
