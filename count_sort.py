import random, copy
from calculate_time import cal_time


@cal_time
def count_sort(li, max_count):
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for idx, val in enumerate(count):
        for _ in range(val):
            li.append(idx)


@cal_time
def sys_sort(li):
    li.sort()


if __name__ == '__main__':
    li = [random.randint(0, 1000) for _ in range(10000)]
    random.shuffle(li)
    li_a = copy.deepcopy(li)
    li_b = copy.deepcopy(li)
    print(li)
    count_sort(li_a, 1000)
    print(li_a)

    sys_sort(li_b)
    print(li_b)
