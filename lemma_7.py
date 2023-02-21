"""
This program uses the ratio of two integers to estimate e using a generator, yielding at every ratio that is a better approximation than the previous
"""

from math import e

def estimate(x=1, y=1):
    previous = x/y
    current = x/y

    while True:
        while abs(e - previous) <= abs(e - current):
            if e - current >= 0:
                y += 1
            else:
                x += 1
            current = x/y
        yield [current, x, y]

if __name__ == "__main__":
    result = next(estimate())
    while (input("hit enter to continue generating, q to quit: ") != 'q'):
        print(f"{result[0]} = {result[1]} / {result[2]}")
        result = next(estimate(result[1], result[2]))
