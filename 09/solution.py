import sys
from functools import cache

files = [open(f"input{i}.txt", "r") for i in [1, 2, 3]]
dataset = [tuple(line.strip() for line in file.readlines()) for file in files]
[f.close() for f in files]

sys.setrecursionlimit(10000)
opts = []


@cache
def construct(n):
    if n == 0:
        return 0
    if n < 0:
        return 10 ** 100
    best = 10 ** 100
    for o in opts:
        sub = construct(n - o)
        best = min(best, 1 + sub)
    return best


def part1(data=dataset[0]):
    global opts
    min_beetles = 0
    opts = [1, 3, 5, 10][::-1]
    for num in map(int, data):
        min_beetles += construct(num)
    print(min_beetles)


def part2(data=dataset[1]):
    global opts
    construct.cache_clear()
    min_beetles = 0
    opts = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30][::-1]
    for num in map(int, data):
        min_beetles += construct(num)
    print(min_beetles)


def part3(data=dataset[2]):
    global opts
    construct.cache_clear()
    min_beetles = 0
    opts = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101][::-1]
    for num in map(int, data):
        n1, n2 = num // 2, num - (num // 2)
        beetles = 1e10
        for i in range(51 - num % 2):
            beetles = min(beetles, construct(n1 - i) + construct(n2 + i))
        min_beetles += beetles
    print(min_beetles)


part1()
part2()
part3()
