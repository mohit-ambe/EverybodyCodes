import re

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    times = dict()
    for line in data:
        i, q, p, t = list(map(int, re.findall("\d+", line)))
        times[i] = times.get(i, 0) + t
    best_times = sorted(times.items(), key=lambda x: x[1])
    print(sum([j * v for j, (k, v) in enumerate(best_times, start=1)]))


def part2(data=dataset[1]):
    times = dict()
    for line in data:
        i, q, p, t = list(map(int, re.findall("\d+", line)))
        t_i = times.get(i, (0, 0))
        times[i] = (t_i[0] + 1, t_i[1] + t)
    best_times = sorted(times.items(), key=lambda x: (-x[1][0], x[1][1]))
    print(sum([j * v[1] for j, (k, v) in enumerate(best_times, start=1)]))


def part3(data=dataset[2]):
    data = [list(map(int, re.findall("\d+", line))) for line in data]
    data.sort(key=lambda d: (d[1], d[2]))
    total_points = dict()
    for quest in range(1, data[-1][1] + 1):
        elapsed = dict()
        for part in range(1, 3 + 1):
            times = [d for d in data if (d[1], d[2]) == (quest, part)]
            for i in range(len(times)):
                times[i][-1] += elapsed.get(times[i][0], 0)
            times.sort(key=lambda t: (t[-1], t[0]))

            points = 50 * part
            prev_time = 0
            for idx, (i, _, _, t) in enumerate(times):
                elapsed[i] = t
                if t != prev_time:
                    points = max(50 * part - idx, 0)
                total_points[i] = total_points.get(i, 0) + points
                prev_time = t

    total_points = sorted(total_points.values(), reverse=True)

    checksum = 0
    rank = 0
    prev_pts = 0
    for idx, pts in enumerate(total_points):
        if pts != prev_pts:
            rank = 1 + idx
        checksum += rank * pts
        prev_pts = pts

    print(checksum)


part1()
part2()
part3()