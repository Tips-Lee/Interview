import random


def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i-1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp


def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i-gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp


def shell_sort(li):
    d = len(li)//2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


if __name__ == '__main__':
    li = list(range(10))
    random.shuffle(li)
    print(li)
    shell_sort(li)
    print(li)