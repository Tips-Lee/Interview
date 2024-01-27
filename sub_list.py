def f(s):
    d = {']': '[', '}': '{', ')': '('}
    stack = []
    for w in s:
        if stack and w in d and d[w] == stack[-1]:
            stack.pop()
        else:
            stack.append(w)
    return len(stack) == 0


print(f('[]{()}}'))
