files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0], p3=False):
    nails = [int(x) for x in data]
    level = (sorted(nails)[len(nails) // 2] if p3 else min(nails))
    print(sum([abs(n - level) for n in nails]))


def part2(data=dataset[1]):
    part1(data)


def part3(data=dataset[2]):
    # the deviations between values in a sample
    # are minimized at the median value
    part1(data, p3=True)


part1()
part2()
part3()
