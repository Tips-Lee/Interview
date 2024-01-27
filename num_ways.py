def num_ways(l):

    m = len(l)
    n = len(l[0])
    start = (0, 0)
    finish = (m-1, n-1)
    stack = [start]
    cnt = 0

    while stack:
        node = stack.pop()
        if node == finish:
            cnt += 1
        if node[0] + 1 < m and node[1] < n and not l[node[0]+1][node[1]]:
            stack.append((node[0]+1, node[1]))
        if node[0] < m and node[1] + 1 < n and not l[node[0]][node[1]+1]:
            stack.append((node[0], node[1]+1))
    return cnt


def num_ways1(l):
    m = len(l)
    n = len(l[0])
    start = (0, 0)
    finish = (m-1, n-1)
    stack = [start]

    c = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if l[i][j] == 1:
                c[i][j] = 0
            elif i == 0 and j == 0:
                c[i][j] = 1
            elif i == 0:
                c[i][j] = c[i][j-1]
            elif j == 0:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i-1][j] + c[i][j-1]

    return c[-1][-1]


def _num_ways2(l, i, j):
    if i == 0 and j == 0:
        return 1
    elif l[i][j] == 1:
        return 0
    elif i == 0:
        return _num_ways2(l, i, j - 1)
    elif j == 0:
        return _num_ways2(l, i - 1, j)
    else:
        return _num_ways2(l, i - 1, j) + _num_ways2(l, i, j - 1)


def num_ways2(l):
    return _num_ways2(l, len(l)-1, len(l[0])-1)


if __name__ == '__main__':
    l = [[0, 0, 0],[0, 1, 0],[0, 0, 0]]
    print(num_ways2(l))