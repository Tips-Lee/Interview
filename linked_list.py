from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, val):
        self.__data = val

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    @property
    def size(self):
        tmp = self.head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def remove(self, item):
        cur = self.head
        prev = None
        found = False
        while cur and not found:
            if cur.data == item:
                found = True
            else:
                prev, cur = cur, cur.next

        if not prev:
            self.head = cur.next
        else:
            prev.next = cur.next

    def __repr__(self):
        tmp = self.head
        ans = []
        while tmp:
            ans.append(str(tmp.data))
            tmp = tmp.next
        return '-->'.join(ans)


class UnorderedList(LinkedList):
    def __init__(self):
        super(UnorderedList, self).__init__()

    def add(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def search(self, item):
        cur = self.head
        found = False
        while cur and not found:
            if cur.data == item:
                found = True
                # return cur
            else:
                cur = cur.next
        return found


class OrderedList(LinkedList):
    def __init__(self):
        super(OrderedList, self).__init__()

    def add(self, val):
        cur = self.head
        prev = None
        stop = False
        while cur and not stop:
            if cur.data > val:
                stop = True
            else:
                prev, cur = cur, cur.next

        tmp = Node(val)
        if not prev:
            tmp.next = self.head
            self.head = tmp
        else:
            prev.next = tmp
            tmp.next = cur

    def search(self, item):
        cur = self.head
        found = False
        stop = False
        while cur and not found and not stop:
            if cur.data == item:
                found = True
            else:
                if cur.data > item:
                    stop = True
                else:
                    cur = cur.next
        return found


if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(4)
    print(node1 <= node2)

    ul = OrderedList()
    ul.add(4)
    ul.add(3)
    ul.add(5)
    print(ul)
    ul.remove(4)
    print(ul)
    ul.add(4)
    print(ul)