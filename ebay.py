
def mul(a, b):
    '''

    :param a:  m * k : list of list
    :param b:  k * n : list of list
    :return:
    '''
    assert len(a[0]) == len(b)

    m = len(a)
    k = len(b)
    n = len(b[0])

    c = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            c[i][j] = sum([a[i][l] * b[l][j] for l in range(k)])
    return c


import random

def sample(l, k=100):
    '''
    :param l: [100, 79 ,...]
    :return:  list of length=100
    '''

    n = len(l)
    l_sum = sum(l)
    frequency = [i/l_sum for i in l]
    for i in range(1, n):
        frequency[i] = frequency[i] + frequency[i-1]

    result = []
    for i in range(k):
        rd_num = random.random()
        for i in range(n):
            if rd_num < frequency[i]:
                result.append(l[i])
                break
    return result


if __name__ == '__main__':
    l = [3, 10, 100, 80]
    print(sample(l))
















