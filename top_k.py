
def sift(li, head, right):
    i = head
    j = 2*i + 1
    tmp = li[head]
    while j <= right:
        if j + 1 <= right and li[j + 1] < li[j]:
            j = j + 1
        if li[j] < li[i]:
            li[i], li[j] = li[j], li[i]
            i, j = j, 2*j + 1
        else:
            break
    # li[i] = tmp


def top_k(li, k):
    # 建一个小堆, 0--k-1
    heap = li[:k]
    i = (k - 2)//2
    for i in range(i, -1, -1):
        sift(heap, i, k-1)

    # 遍历 k--n-1,跟前面建立的堆进行比较，剔除或者添加
    for i in range(k, len(li)):
        if li[i] < li[0]:
            continue
        if li[i] > li[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)

    # 堆排序
    j = k-1
    while j > 0:
        heap[j], heap[0] = heap[0], heap[j]
        j -= 1
        sift(heap, 0, j)
    return heap


if __name__ == '__main__':
    li = [3, 1, 5, 2, 4, 8, 6, 7, 9, 12, 11, 13, 10]
    print(top_k(li, 4))
    # print(li)