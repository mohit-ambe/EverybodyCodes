from heapq import heappop, heappush

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

directions = {"U":(0, 1, 0), "D":(0, -1, 0), "R":(1, 0, 0), "L":(-1, 0, 0), "F":(0, 0, 1), "B":(0, 0, -1)}


def draw_segments(instructions):
    height, blocks = 0, set()
    x, y, z = 0, 0, 0
    for inst in instructions:
        d = inst[0]
        r = int(inst[1:])
        dx, dy, dz = directions[d]
        blocks |= {(x := x + dx, y := y + dy, z := z + dz) for _ in range(r)}
        height = max(height, y)
    return height, blocks, {(x, y, z)}


def part1(data=dataset[0]):
    print(draw_segments(data[0].split(","))[0])


def part2(data=dataset[1]):
    blocks = set()
    for line in data:
        blocks |= draw_segments(line.split(","))[1]
    print(len(blocks))


def part3(data=dataset[2]):
    height, blocks, leaves = 0, set(), set()
    for line in data:
        h, b, l = draw_segments(line.split(","))
        height = max(height, h)
        blocks |= b
        leaves |= l

    # find the min distance for every leaf-root pair
    trunk_to_leaf = {(0, yy, 0):dict() for yy in range(1, height + 1)}
    for leaf in leaves:
        Q = [(0, leaf)]
        visited = set()
        while Q:
            d, (x, y, z) = heappop(Q)

            if (x, y, z) == (0, y, 0):
                trunk_to_leaf[(x, y, z)][leaf] = min(trunk_to_leaf[(x, y, z)].get(leaf, 1000), d)

            if (x, y, z) in visited:
                continue
            visited.add((x, y, z))

            for dx, dy, dz in directions.values():
                np = (x + dx, y + dy, z + dz)
                if np in blocks:
                    heappush(Q, (d + 1, np))

    # return the min total distance for a trunk segment to all leaves
    print(min(sum(trunk_to_leaf[rt].values()) for rt in trunk_to_leaf if trunk_to_leaf[rt]))


part1()
part2()
part3()
