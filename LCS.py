from pprint import pprint
def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    r = [['O' for _ in range(n+1)] for _ in range(m+1)]  # 0 终止， 1：左上， 2：左，3：上
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                r[i][j] = 'X'
            else:
                if c[i][j-1] >= c[i-1][j]:
                    r[i][j] = '<'
                    c[i][j] = c[i][j-1]
                else:
                    r[i][j] = '^'
                    c[i][j] = c[i-1][j]
    return c, r


def decode_lcs(r, s1):
    i = len(r)-1
    j = len(r[0])-1
    result = ''
    while r[i][j] != 'O':
        if r[i][j] == 'X':
            result += s1[i-1]
            i, j = i-1, j-1
        elif r[i][j] == '<':
            j = j - 1
        else:
            i = i - 1
    return ''.join(reversed(result))



if __name__ == '__main__':
    s1 = 'abcdef'
    s2 = 'acdagfb'
    # return acd
    c, r = lcs(s1, s2)
    pprint(c)
    pprint(r)
    pprint(decode_lcs(r, s1))