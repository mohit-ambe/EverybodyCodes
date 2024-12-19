from functools import cache

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

directions = [(-1, 0), (-0, 1), (1, -0), (0, -1)]


def part1(data=dataset[0]):
    words = data[0][data[0].index(":") + 1:].split(",")
    sentence = data[2]
    print(sum([sentence.count(word) for word in words]))


def part2(data=dataset[1]):
    words = set(data[0][data[0].index(":") + 1:].split(","))
    lines = data[2:]
    runic = 0
    for line in lines:
        indices = set()
        for word in [w for w in words if w in line or w[::-1] in line]:
            for i in range(len(line) - len(word) + 1):
                if line[i:i + len(word)] in [word, word[::-1]]:
                    indices |= {i for i in range(i, i + len(word))}
        runic += len(indices)
    print(runic)


@cache
def find_sources(map, target):
    sources = set()
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == target:
                sources.add((0, y, x, 0, 0))
    return sources


def part3(data=dataset[2]):
    words = set(data[0][data[0].index(":") + 1:].split(","))
    lines = data[2:]
    runic = set()
    for word in words:
        Q = [(*s, []) for s in find_sources(lines, word[0])]
        if len(word) == 1:
            runic |= {(q[1], q[2]) for q in Q}
            continue
        visited = set()
        while Q:
            Q.sort(key=lambda n: n[0], reverse=True)
            i, y, x, dy, dx, path = Q.pop(0)

            if i == len(word):
                runic |= set(path)
                continue
            path.append((y, x))

            if not (0 <= y < len(lines)):
                continue
            if lines[y][x] != word[i]:
                continue
            if (y, x, dy, dx) in visited:
                continue
            visited.add((y, x, dy, dx))

            if i == 0:
                for ddy, ddx in directions:
                    Q.append((i + 1, y + ddy, (x + ddx) % len(lines[0]), ddy, ddx, path.copy()))
            else:
                Q.append((i + 1, y + dy, (x + dx) % len(lines[0]), dy, dx, path.copy()))

    print(len(runic))


part1()
part2()
part3()
