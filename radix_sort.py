import random
import copy
from count_sort import sys_sort
from calculate_time import cal_time
from quick_sort import quick_sort

@cal_time
def redix_sort(li):
    max_num = max(li)
    t = 0
    while 10 ** t <= max_num:
        buckets = [[] for _ in range(10)]
        for val in li:
            idx = (val//10**t) % 10
            buckets[idx].append(val)
        li.clear()
        for buc in buckets:
            li.extend(buc)
        t += 1


if __name__ == '__main__':
    random.seed(10)
    li = [random.randint(0, 100000) for _ in range(50000)]
    random.shuffle(li)
    li_a = copy.deepcopy(li)
    li_b = copy.deepcopy(li)
    li_c = copy.deepcopy(li)
    print(li)
    redix_sort(li_a)
    print(li_a)
    quick_sort(li_b)
    print(li_b)
    sys_sort(li_c)
    print(li_c)
