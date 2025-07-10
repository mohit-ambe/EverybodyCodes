from heapq import heappop, heappush

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
height = lambda a, b:min(abs(a - b), abs(a - b + 10), abs(a - b - 10))


def pathfind(data, end_as_source=False):
    maze = {(y, x):data[y][x] for y in range(len(data)) for x in range(len(data[0])) if data[y][x] not in " #"}
    inv = {v:k for k, v in maze.items()}

    start = (0, 0)
    if not end_as_source:
        start = inv['S']
    end = inv['E']
    maze = {k:0 if v in 'SE' else int(v) for k, v in maze.items()}

    Q = [(0, start if not end_as_source else end)]
    visited = set()
    dist = sum(maze.values())

    while Q:
        d, (y, x) = heappop(Q)
        if data[y][x] == ("E" if not end_as_source else "S"):
            dist = min(dist, d)
            continue

        if d > dist:
            continue

        if (y, x) in visited:
            continue
        visited.add((y, x))

        for dy, dx in directions:
            np = (y + dy, x + dx)
            if np in maze:
                levels = height(maze[np], maze[(y, x)])
                heappush(Q, (d + 1 + levels, np))

    return dist


def part1(data=dataset[0]):
    print(pathfind(data))


def part2(data=dataset[1]):
    print(pathfind(data))


def part3(data=dataset[2]):
    print(pathfind(data, end_as_source=True))


part1()
part2()
part3()
