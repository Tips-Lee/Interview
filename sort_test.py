import tensorflow as tf
import numpy as np
import heapq
import numpy as np
import tensorflow as tf
from functools import cmp_to_key

'''
def next_batch():
    datasets = np.asarray(range(0, 20))
    input_queue = tf.train.slice_input_producer([datasets], shuffle=False, num_epochs=1)
    data_batchs = tf.train.batch(input_queue, batch_size=5, num_threads=1,
                                 capacity=20, allow_smaller_final_batch=False)
    return data_batchs

if __name__ == "__main__":
    # data_batchs = next_batch()
    datasets =tf.convert_to_tensor(np.asarray(range(0, 40)).reshape(20,2))
    # print(datasets)
    input_queue = tf.train.slice_input_producer([datasets], shuffle=False, num_epochs=1)
    data_batchs = tf.train.batch(input_queue, batch_size=5, num_threads=4, capacity=5, allow_smaller_final_batch=True, enqueue_many=True)

    sess = tf.Session()
    sess.run(tf.local_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess, coord)
    try:
        while not coord.should_stop():
            data = sess.run([data_batchs])
            print(data)
    except tf.errors.OutOfRangeError:
        print("complete")
    finally:
        coord.request_stop()
    coord.join(threads)
    sess.close()
'''


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print('move plate from %s to %s' % (a, c))
        hanoi(n-1, b, a, c)


def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[min_loc], li[i] = li[i], li[min_loc]


def insert_sort(li):
    for i in range(1, len(li)):
        j = i-1
        tmp = li[i]
        while j >= 0 and li[j] > li[i]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while li[right] >= tmp and left < right:
            right -= 1
        li[left] = li[right]
        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ans = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            ans.append(li[i])
            i += 1
        else:
            ans.append(li[j])
            j += 1
    if i <= mid:
        ans += li[i: mid + 1]
    if j <= high:
        ans += li[j: high+1]
    li[low: high+1] = ans


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)


def max_price(goods, w):

    total_value = 0
    m = [0 for _ in goods]
    for i, (price, weight) in enumerate(goods):
        if w >= weight:
            w -= weight
            m[i] = 1
            total_value += price
        else:
            part = w/weight
            m[i] = part
            total_value += price * w / weight

    return total_value, m


def xy_cmp(x, y):
    if x + y > y + x:
        return 1
    elif x + y == y + x:
        return 0
    else:
        return -1


def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp), reverse=True)
    return int(''.join(li))


def activity_select(activity):
    a = sorted(activity, key=lambda x: x[1])
    ans = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= ans[-1][-1]:
            ans.append(a[i])
    return ans


def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    return fibnacci(n-1) + fibnacci(n-2)


def quick_fibnacci(n):
    ans = [0, 1, 1]
    if n > 2:
        for i in range(n-2):
            ans.append(ans[-1] + ans[-2])
    return ans[n]


def cut_rod(n, p):
    r = p[0]
    for i in range(1, n+1):
        # r = max(r, cut_rod(i, p) + cut_rod(n-i, p))
        r = max(r, p[i] + cut_rod(n-i, p))
    return r


def quick_cut_rod(n, p):
    r_list = [0]
    if n >= 1:
        for i in range(1, n+1):
            r = 0
            for j in range(1, i+1):
                r = max(r, p[j] + r_list[i-j])
            r_list.append(r)
    return r_list[-1]


def quick_cut_rod_sequence(n, p):
    r_list = [0]
    s_list = [0]
    if n >= 1:
        for i in range(1, n+1):
            r = 0
            s = None
            for j in range(1, i+1):
                if p[j] + r_list[i-j] > r:
                    r = p[j] + r_list[i-j]
                    s = j
            r_list.append(r)
            s_list.append(s)
    return r_list[-1], s_list


def cut_rod_solution(n, p):
    r, s_list = quick_cut_rod_sequence(n, p)
    ans = []
    while n > 0:
        s = s_list[n]
        n -= s
        ans.append(s)
    return ans


def lcs_length(x, y):
    m, n = len(x), len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                s[i][j] = 3
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                s[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                s[i][j] = 1

    return c[-1][-1], s


def lcs_trace(x, y):
    c, s = lcs_length(x, y)
    m, n = len(x), len(y)
    ans = []
    i = m
    j = n
    while i > 0 and j > 0:
        if s[i][j] == 3:
            ans.append(x[i-1])
            i -= 1
            j -= 1
        elif s[i][j] == 2:
            i -= 1
        else:
            j -= 1
    ans = ''.join(reversed(ans))
    return ans


def gcd(x, y):
    while x % y != 0:
        x, y = y, x % y
    else:
        return y


class Fraction:
    def __init__(self, a, b):
        r = self.gcd(a, b)
        self.a = a/r
        self.b = b/r

    @staticmethod
    def gcd(x, y):
        while x % y != 0:
            x, y = y, x % y
        else:
            return y

    def __str__(self):
        return '%d/%d' % (self.a, self.b)

    def __repr__(self):
        return '%d//%d' % (self.a, self.b)


def sift(li, low, high):
    i = low
    tmp = li[low]
    j = 2 * i + 1
    while j <= high:
        if j + 1 <= high and li[j + 1] > li[j]:
            j += 1
        if tmp < li[j]:
            li[i] = li[j]
            i, j = j, 2*j + 1
        else:
            break
    li[i] = tmp


def heap_sort(li):
    n = len(li)
    high = n-1
    for i in range((n-2)//2, -1, -1):
        sift(li, i, high)

    for j in range(high, -1, -1):
        li[0], li[j] = li[j], li[0]
        sift(li, 0, j-1)


if __name__ == '__main__':
    # hanoi(3, 'A', 'B', 'C')
    li = [3, 4, 1, 2, 5]
    # li = [32, 94, 128, 1286, 6, 71]
    # activity = [(1,4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    # p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # select_sort(li)
    # insert_sort(li)
    # quick_sort(li, 0 , len(li)-1)
    # merge_sort(li, 0, 4)
    # merge(li, 0, 1, 4)
    # li.reverse()
    # li = number_join(li)
    # ans = activity_select(activity)
    # for i in range(1, 8):
    #     print(quick_fibnacci(i))

    # goods = [(60, 10), (200, 50), (100, 20)]
    # goods.sort(key=lambda x: x[0]/x[1], reverse=True)
    # print(max_price(goods, 40))
    # x = 'ABCBDAB'
    # y = 'BDCABA'
    # print(lcs_length(x, y))
    # print(lcs_trace(x, y))
    # print(cut_rod_solution(9, p))
    # print(gcd(60, 21))
    # frac = Fraction(60, 21)
    # print(frac)
    # heap_sort(li)
    # print(li)
    # dic = {'a':1, 'b':2}
    # print(dic.get('c'))




