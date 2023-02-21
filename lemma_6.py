"""
This program determines optimal values to minimize |x^(1/e) - y^(1/pi)| using a generator that yields the next best integer approximation for x and y
"""

from math import e, pi

def estimate(x=2, y=0):
    previous = x**(1/e) - y**(1/pi)
    current = x**(1/e) - y**(1/pi)

    while True:
        while (abs(previous) <= abs(current)):
            if (current > 0):
                y += 1
            else:
                x += 1
            current = x**(1/e) - y**(1/pi)
        yield [current, x, y]


if __name__ == "__main__":
    result = next(estimate())
    while (input("hit enter to continue generating, q to quit: ") != 'q'):
        print(f"{result[0]} = {result[1]}^(1/e) - {result[2]}&(1/pi)")
        result = next(estimate(result[1], result[2]))
