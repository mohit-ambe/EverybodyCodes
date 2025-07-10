from heapq import heappop, heappush

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def pathfind(data, start):
    obstacles = {"#", "~"}
    maze = {(y, x) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] not in obstacles}
    herbs = set("".join(data)) - obstacles
    Q = [(0, start, set())]
    visited = set()
    dist = 10000

    while Q:
        d, (y, x), h = heappop(Q)
        if (y, x) == start and h == herbs:
            dist = min(dist, d)
            continue

        herb_code = "".join(sorted(h))
        if (y, x, herb_code) in visited:
            continue
        visited.add((y, x, herb_code))

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            np = (y + dy, x + dx)
            if np in maze:
                nh = h | {data[y][x]} - obstacles
                heappush(Q, (d + 1, np, nh))

    return dist


def part1(data=dataset[0]):
    start = (0, data[0].index("."))
    print(pathfind(data, start))


def part2(data=dataset[1]):
    start = (0, data[0].index("."))
    print(pathfind(data, start))


def part3(data=dataset[2]):
    # to reduce search space, split the input into 3 maps

    left = [line[:86] for line in data]
    right = [line[-86:] for line in data]

    center = [line[85:-85] for line in data]
    # replace one of the herbs with another letter,
    # so pathfind() will travel to both sides of the center map
    center[-2] = center[-2].replace("K", "X", 1)

    left_entrance = (len(left) - 2, len(left[0]) - 1)
    L = pathfind(left, left_entrance)

    center_entrance = (0, center[0].index("."))
    C = pathfind(center, center_entrance)

    right_entrance = (len(right) - 2, 0)
    R = pathfind(right, right_entrance)

    # total steps =
    # left + 1 (enter) + 1 (leave)
    # + center +
    # right + 1 (enter) + 1 (leave)
    print(L + C + R + 4)


part1()
part2()
part3()
