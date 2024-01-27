# ! usr/bin/python
# File Name : stock.py
__author__ = 'Tips'


def get_profit(L):
    n = len(L)
    i, j = 0, 0
    profit, new_profit = 0, 0
    for k in range(n):
        if L[k] > L[j]:
            j = k
            new_profit = L[j] - L[i]
        if L[k] < L[i]:
            i, j = k, k
            continue
        if new_profit > profit:
            profit = new_profit
    return profit


def get_profit1(L):
    n = len(L)
    i, j = 0, 0
    profit = 0
    for k in range(n):
        if L[k] >= L[i]:
            profit = max(profit, L[k] - L[i])
        if L[k] < L[i]:
            i = k
    return profit


def get_profit2(L):
    n = len(L)
    i, j = 0, 0
    profit = 0
    for j in range(n):
        if L[j] >= L[i]:
            profit = max(profit, L[j] - L[i])
        if L[j] < L[i]:
            i = j
    return profit


if __name__ == '__main__':
    L = [2, 3, 9, 6, 50, -1, 49]

    profit = get_profit2(L)
    print(profit)
