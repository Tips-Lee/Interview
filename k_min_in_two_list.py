

def kth_min(l1, l2, k):
    m = len(l1)
    n = len(l2)
    i = 0
    u = k if k <= m else m
    mid = (i + u)//2
    j = k - 2 - mid
    if j < 0:
        return l1[mid]
    if j >= n:
        mid = k - n - 1
        j = n - 1
        u = m - 1
    while l1[mid+1] <= l2[j] or l1[mid] > l2[j+1]:
        if j < 0:
            return l1[mid]
        if j >= n:
            mid = k - n - 1
            j = n - 1
            u = m - 1
        if l1[mid+1] <= l2[j]:
            i = mid - 1
            mid = (i + u) // 2
            j = k - 2 - mid
        elif l2[mid] > l2[j+1]:
            u = mid + 1
            mid = (i + u) // 2
            j = k - 2 - mid
    else:
        ans = max(l1[mid], l2[j])
    return ans


if __name__ == '__main__':
    l1 = [1, 2, 2, 3, 5, 7]
    l2 = [3, 4, 8]
    k = 3
    ans = kth_min(l1, l2, k)
    print(ans)