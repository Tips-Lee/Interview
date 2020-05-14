from calculate_time import cal_time


def split(li, left, right):
    tmp = li[left]
    i, j = left, right
    while i < j:
        while li[j] >= tmp and i < j:
            j -= 1
        li[i] = li[j]
        while li[i] <= tmp and i < j:
            i += 1
        li[j] = li[i]
    li[i] = tmp
    return i


def __quick_sort(li, left, right):
    if left < right:
        pos = split(li, left, right)
        __quick_sort(li, left, pos-1)
        __quick_sort(li, pos+1, right)


@cal_time
def quick_sort(li):
    __quick_sort(li, 0, len(li) - 1)


if __name__ == '__main__':
    li = [3, 1, 5, 2, 4]
    quick_sort(li)
    print(li)
    sorted()