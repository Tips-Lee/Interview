

def merge(li, left, mid, right):
    i, j = left, mid + 1
    ans = []
    while i <= mid and j <= right:
        if li[i] <= li[j]:
            ans.append(li[i])
            i += 1
        else:
            ans.append(li[j])
            j += 1
    if i <= mid:
        ans += li[i: mid + 1]
    if j <= right:
        ans += li[j: right+1]
    li[left: right+1] = ans


def merge_sort(li, left, right):
    if left < right:
        mid = (left + right)//2
        merge_sort(li, left, mid)
        merge_sort(li, mid+1, right)
        merge(li, left, mid, right)


if __name__ == '__main__':
    li = [3, 1, 5, 2, 4]
    merge_sort(li, 0, len(li)-1)
    print(li)