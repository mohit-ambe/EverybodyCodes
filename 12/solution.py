from functools import cache

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

ranks = {'A':1, 'B':2, 'C':3}
launch_locs = {(2, 0):"C", (1, 0):"B", (0, 0):"A"}


def get_ranking(data, targets):
    ranking = 0
    for (y, x), r in launch_locs.items():
        for power in range(1, len(data[0])):
            dy, dx = y + power, x + power * 2
            for i in range(dy + 1):
                possible = (dy - i, dx + i)
                if targets.get(possible, -1) > 0:
                    ranking += ranks[r] * power * targets[possible]
                    targets[possible] = 0
    return ranking


def part1(data=dataset[0]):
    # normalize so that A is origin, +x is right, +y is up
    targets = {(len(data) - y - 2, x - 1):1 for y in range(len(data)) for x, l in enumerate(data[y]) if l in "T"}
    print(get_ranking(data, targets))


def part2(data=dataset[1]):
    # normalize so that A is origin, +x is right, +y is up
    targets = {(len(data) - y - 2, x - 1):(2 if l == "H" else 1) for y in range(len(data)) for x, l in enumerate(data[y]) if l in "TH"}
    print(get_ranking(data, targets))


@cache
def shot_path(yi, power):
    y, x = yi, 0
    path = {0:(y, x)}
    t = 0
    for i in range(power):
        y, x = y + 1, x + 1
        t += 1
        path[(y, x)] = t
    for i in range(power):
        y, x = y, x + 1
        t += 1
        path[(y, x)] = t
    for i in range(y):
        y, x = y - 1, x + 1
        t += 1
        path[(y, x)] = t
    return path


# ~3 minute runtime
def part3(data=dataset[2]):
    targets = [tuple(map(int, line.split()[::-1])) for line in data]
    total_ranking = 0

    for (y, x) in targets:
        rank_alt = set()
        meteor = {(y - i, x - i):i for i in range(y + 1)}
        for y0, x0 in sorted(launch_locs):
            for power in range(y // 2, 0, -1):
                shot = shot_path(y0, power)
                if intersection := shot.keys() & meteor.keys():
                    my, mx = sorted(intersection)[-1]
                    if shot[(my, mx)] > meteor[(my, mx)]:
                        continue
                    rank_alt.add((my, power * ranks[launch_locs[(y0, x0)]]))
        total_ranking += sorted(rank_alt, key=lambda k:(k[0], -k[1]))[-1][1]

    print(total_ranking)


part1()
part2()
part3()
