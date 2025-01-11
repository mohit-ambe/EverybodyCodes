files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def pyramid_size(base):
    return ((base + 1) // 2) ** 2


def part1(data=dataset[0]):
    num = int(data[0])
    base = 1
    while num > pyramid_size(base):
        base += 2
    print((pyramid_size(base) - num) * base)


def part2(data=dataset[1]):
    supply = 20240000
    high_priests = int(data[0])
    acolytes = 1111
    thickness = 1
    base = 1
    while supply - thickness > 0:
        supply -= thickness * base
        thickness = (thickness * high_priests) % acolytes
        base += 2
    print((base - 2) * -supply)


def part3(data=dataset[2]):
    supply = 202400000
    high_priests = int(data[0])
    acolytes = 10
    thickness = 1
    width = 1
    layer = 1
    heights = [0]
    while True:
        heights = [0] + [i + thickness for i in heights] + [0]
        hole = [(high_priests * width * h) % acolytes for h in heights[2:-2]]
        width += 2
        thickness = ((thickness * high_priests) % acolytes) + acolytes
        cost = sum(heights) - sum(hole)
        layer += 1

        if cost > supply:
            print(cost - supply)
            break


part1()
part2()
part3()
