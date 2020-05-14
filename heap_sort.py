
def sift(li, head, right):
    i = head
    j = 2*i + 1
    tmp = li[head]
    while j <= right:
        if j + 1 <= right and li[j + 1] > li[j]:
            j = j + 1
        if li[j] > li[i]:
            li[i], li[j] = li[j], li[i]
            i, j = j, 2*j + 1
        else:
            break
    # li[i] = tmp


def heap_sort(li):
    # 建一个堆
    i = (len(li) - 2)//2
    for i in range(i, -1, -1):
        sift(li, i, len(li)-1)
    # 堆排序
    j = len(li)-1
    while j > 0:
        li[j], li[0] = li[0], li[j]
        j -= 1
        sift(li, 0, j)


if __name__ == '__main__':
    li = [3, 1, 5, 2, 4, 8, 6, 7]
    heap_sort(li)
    print(li)