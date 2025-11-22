from itertools import combinations

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def is_child(child, p1, p2):
    for char in range(len(child)):
        if child[char] not in [p1[char], p2[char]]:
            return False
    return True


def part1(data=dataset[0], lines=None):
    if data is None:
        dna = lines.copy()
    else:
        dna = [d[d.index(":") + 1:] for d in data]

    sim = 1
    for i in range(len(dna) - 1):
        sim *= len([x for x in range(len(dna[i])) if dna[i][x] == dna[-1][x]])

    if lines is None:
        print(sim)
    else:
        return sim


def part2(data=dataset[1]):
    dna = [d[d.index(":") + 1:] for d in data]
    sim = 0

    for i, j, k in combinations([x for x in range(1, len(dna) + 1)], 3):
        a, b, c = dna[i - 1], dna[j - 1], dna[k - 1]
        if is_child(a, b, c):
            sim += part1(None, [b, c, a])
        if is_child(b, a, c):
            sim += part1(None, [a, c, b])
        if is_child(c, a, b):
            sim += part1(None, [a, b, c])

    print(sim)


def part3(data=dataset[2]):
    dna = [d[d.index(":") + 1:] for d in data]

    # find all relationships
    fams = []
    for i, j, k in combinations([x for x in range(1, len(dna) + 1)], 3):
        a, b, c = dna[i - 1], dna[j - 1], dna[k - 1]
        if is_child(a, b, c) or is_child(b, a, c) or is_child(c, a, b):
            fams.append({i, j, k})

    # join the relationships
    change = True
    while change:
        change = False
        x = 0
        while x < len(fams):
            y = x + 1
            while y < len(fams):
                if fams[x] & fams[y] != set():
                    change = True
                    fams[x] |= fams[y]
                    fams.pop(y)
                    y -= 1
                y += 1
            x += 1

    print(sum(max([x for x in fams], key=len)))


part1()
part2()
part3()
