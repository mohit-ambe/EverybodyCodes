import functools
import math

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]


def part1(data=dataset[0]):
    print(sum(map(lambda x: math.ceil(int(x) ** 0.5) ** 2 - int(x), data[0].split(","))))


def part2(data=dataset[1]):
    nums = list(map(int, data[0].split(",")))
    frame_size = lambda n: n ** 2 - (n - 2) ** 2
    frame_size = functools.cache(frame_size)
    total = 0

    for num in nums:
        for i in range(3, max(nums)):
            fsi = frame_size(i)
            if fsi >= num:
                total += max(fsi - num, 0)
                break

    print(total)


def part3(data=dataset[2]):
    nums = list(map(int, data[0].split(",")))
    frame_size = lambda n: n ** 2 - 1
    frame_size = functools.cache(frame_size)
    total = 0

    for num in nums:
        for i in range(3, max(nums), 2):
            fsi = frame_size(i)
            if fsi >= num:
                total += max(fsi - num, 0)
                break

    print(total)


part1()
part2()
part3()