files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

parse = lambda d:{k:v.split(",") for l in d for k, v in [l.split(":")]}


def simulate(rules, termites, days):
    rules = parse(rules)
    for _ in range(days):
        new_termites = {}
        for t in termites.copy():
            for nt in rules[t]:
                new_termites[nt] = new_termites.get(nt, 0) + termites[t]
        termites = new_termites.copy()
    return sum(termites.values())


def part1(data=dataset[0]):
    print(simulate(data, {"A":1}, 4))


def part2(data=dataset[1]):
    print(simulate(data, {"Z":1}, 10))


def part3(data=dataset[2]):
    rules = parse(data)
    min_t, max_t = 1e15, 0
    for r in rules:
        population = simulate(data, {r:1}, 20)
        min_t = min(min_t, population)
        max_t = max(max_t, population)
    print(max_t - min_t)


part1()
part2()
part3()
