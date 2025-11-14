files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

add = lambda a, b: [a[0] + b[0], a[1] + b[1]]
mul = lambda a, b: [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]]
div = lambda a, b: [int(a[0] / b[0]), int(a[1] / b[1])]


def count_engravings(a, spacing=1):
    engraved = 0

    for y in range(a[1], a[1] + 1000 + 1, spacing):
        for x in range(a[0], a[0] + 1000 + 1, spacing):
            r = [0, 0]
            overflow = False
            for c in range(100):
                r = mul(r, r)
                r = div(r, [1e5, 1e5])
                r = add(r, [x, y])
                if any([abs(rr) > 1e6 for rr in r]):
                    overflow = True
                    break
            if not overflow:
                engraved += 1

    return engraved


def part1(data=dataset[0]):
    a = eval(data[0][2:])
    r = [0, 0]
    for _ in range(3):
        r = mul(r, r)
        r = div(r, [10, 10])
        r = add(r, a)
    print(str(r).replace(" ", ""))


def part2(data=dataset[1]):
    a = eval(data[0][2:])
    print(count_engravings(a, 1000 // 100))


def part3(data=dataset[2]):
    # brute force (takes a while)
    a = eval(data[0][2:])
    print(count_engravings(a))


part1()
part2()
part3()
