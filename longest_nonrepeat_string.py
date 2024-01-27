import pandas as pd
import numpy as np

'''
def longest(s):
    m = len(s)
    ans = []
    for i in range(m):
        tmp = s[i]
        for j in range(i+1, m):
            if s[j] in tmp:
                break
            else:
                tmp += s[j]
        ans.append(len(tmp))
    return max(ans)
'''

'''
问题：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

'''
def is_unique(s):
    s1 = set(list(s))
    return len(s) == len(s1)


def longest(s):
    i, j = 0, 1
    max_str = 0
    length = len(s)
    while j < length:
        tmp = s[i:j+1]
        if is_unique(tmp):
            max_str = max(max_str, len(tmp))
            j += 1
        else:
            i += 1
    return max_str
'''

'''
def longest(s):
    i, j = 0, 1
    max_str = 0
    length = len(s)
    if len(s) == 0 or len(s) == 1:
        return len(s)

    while j < length:
        tmp = s[i:j]
        if s[j] not in tmp:
            max_str = max(max_str, j-i+1)
            j += 1
        else:
            i += 1
    return max_str
'''


def longest(s):
    cache = {}
    max_str = 0
    start = 0
    for idx, string in enumerate(s):
        if string in cache and cache[string] >= start:
            start = cache[string] + 1
            cache[string] = idx
        else:
            cache[string] = idx
            max_str = max(max_str, idx - start + 1)
    return max_str


if __name__ == '__main__':
    test_str = 'pwwkew'
    # test_str = 'bbbb'
    # test_str = 'abcabcbb'
    print(longest(test_str))
