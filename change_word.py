def min_change(a, b):
    m = len(a)
    n = len(b)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                c[i][j] = c[i - 1][j - 1]
            else:
                c[i][j] = min(c[i - 1][j - 1], c[i][j - 1], c[i - 1][j]) + 1

    return c[m][n]


if __name__ == '__main__':
    a = 'horse'
    b = 'post'
    ans = min_change(a, b)
    print(ans)
