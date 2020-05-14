

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def convert(num, digit):
    digits = '0123456789ABCDEF'
    s = Stack()
    ans = ''
    while num > 0:
        val = num % digit
        s.push(val)
        num //= digit
    while not s.isEmpty():
        val = s.pop()
        ans += digits[val]
    return ans


if __name__ == '__main__':
    s = Stack()
    print(convert(18, 16))