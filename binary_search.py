import random
import copy
from count_sort import sys_sort
from calculate_time import cal_time
from quick_sort import quick_sort


@cal_time
def linear_search(li, val):
    for idx, value in enumerate(li):
        if val == value:
            return idx
    raise ValueError('%s is not in list' % str(val))


@cal_time
def binary_search(li, val):
    left = 0
    right = len(li)-1
    while left <= right:
        mid = (left + right)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    raise ValueError('%s is not in list' % str(val))


if __name__ == '__main__':
    # random.seed(110)
    # li = [random.randint(0, 100) for _ in range(1000)]
    # random.shuffle(li)
    li = list(range(1, 100000))
    print(li)
    # print(li.index(4))
    print(binary_search(li, 88888))
    print(linear_search(li, 88888))
