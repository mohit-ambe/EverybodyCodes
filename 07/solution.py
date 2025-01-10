from itertools import permutations

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

directions = [(-1, 0), (-0, 1), (1, -0), (0, -1)]
tracks = ['', '', '']
tracks[0] = "========="
tracks[1] = "\
-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=---=++==--\
+++==++=+=--==++==+++=++=+++=--=+=-=+=-+=-+=-+-=+=-=+=-+++=+==++++==---=+=+=-="
tracks[2] = "\
+=+++===-+++++=-==+--+=+===-++=====+--===++=-==+=++====-==-===+=+=--==++=+========-==\
=====++--+++=-++=-+=+==-=++=--+=-====++--+=-==++======+=++=-+==+=-==++=-=-=---++=-=++\
==++===--==+===++===---+++==++=+=-=====+==++===--==-==+++==+++=++=+===--==++--===+===\
==-=++====-+=-+--=+++=-+-===++====+++--=++====+=-=+===+=====-+++=+==++++==----=+=+=-="


def race(track, laps, line):
    plan, actions = line.split(":")
    actions = actions.split(",")
    total_power = 0
    power = 10
    i = 0
    for _ in range(laps):
        for t in track:
            if t == '=':
                t = actions[i % len(actions)]
            if t == '+':
                power += 1
            elif t == '-':
                power -= 1
            total_power += power
            i += 1
    return plan, total_power


def part1(data=dataset[0]):
    plans = dict()
    for line in data:
        plan, power = race(tracks[0], 1, line)
        plans[plan] = power
    items = sorted(plans.items(), key=lambda i: i[1], reverse=True)
    print("".join([i[0] for i in items]))


def part2(data=dataset[1]):
    plans = dict()
    for line in data:
        plan, power = race(tracks[1], 10, line)
        plans[plan] = power
    items = sorted(plans.items(), key=lambda i: i[1], reverse=True)
    print("".join([i[0] for i in items]))


def part3(data=dataset[2]):
    # the alignment of the track and
    # the action plan loops after 11 laps,
    # so only the first 11 are needed to
    # determine a winner

    _, king = race(tracks[2], 11, data[0])
    winning = 0
    action_plans = set(permutations("+++++---==="))
    for i, p in enumerate(action_plans):
        p = "K:" + ",".join(p)
        if race(tracks[2], 11, p)[1] > king:
            winning += 1
    print(winning)


part1()
part2()
part3()
