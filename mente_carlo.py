import random


def cal_pi():
    a, b = 0.0, 0.0
    r = 1.0
    r_neg = a - r
    r_pos = b + r

    count = 0
    step = 10000000
    for i in range(step):
        x = random.uniform(r_neg, r_pos)
        y = random.uniform(r_neg, r_pos)
        if (x - a)**2 + (y - b)**2 <= r**2:
            count += 1
    return count / step * 4


def g(x):
    return x**2

def integral():
    a = 0
    b = 1
    n = 100000
    total = 0
    for i in range(n):
        x = random.uniform(a, b)
        y = g(x)
        total += y
    return total * (b - a)/n


if __name__ == '__main__':
    # print(cal_pi())
    print(integral())
