import numpy as np


def bag(item, C):
    m = len(item)
    n = C
    f = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if j >= item[i-1][1]:
                f[i][j] = max(f[i-1][j], f[i-1][j-item[i-1][1]] + item[i-1][0])
            else:
                f[i][j] = f[i-1][j]
    return f[m][n], f


if __name__ == '__main__':
    v = [8, 10, 6, 3, 7, 2]
    w = [4, 6, 2, 2, 5, 1]
    C = 12
    item = [(i, j) for i, j in zip(v, w)]
    # item.sort(key=lambda x: x[1], reverse=False)
    print(item)
    ans, mat = bag(item, C)
    print(ans)
    print(np.asarray(mat))