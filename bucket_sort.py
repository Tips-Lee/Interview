import random
import copy
from count_sort import sys_sort
from calculate_time import cal_time


@cal_time
def bucket_sort(li, n=100):
    buckets = [[] for _ in range(n)]
    max_num = max(li)
    for val in li:
        id = min(n-1, val//(max_num//n))
        buckets[id].append(val)
        i = len(buckets[id]) - 2
        while i >= 0 and buckets[id][i] > val:
            buckets[id][i+1] = buckets[id][i]
            i -= 1
        buckets[id][i + 1] = val

    li.clear()
    for buc in buckets:
        li.extend(buc)


if __name__ == '__main__':
    random.seed(10)
    li = [random.randint(0, 10000) for _ in range(20000)]
    random.shuffle(li)
    li_a = copy.deepcopy(li)
    li_b = copy.deepcopy(li)
    print(li)
    bucket_sort(li_a, 1000)
    print(li_a)
    sys_sort(li_b)
    print(li_b)



