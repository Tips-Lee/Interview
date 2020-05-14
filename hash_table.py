from collections import Iterable, Iterator


'''
class HashLinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, head):
            self.head = head

        def __iter__(self):
            return self

        def __next__(self):
            if self.head:
                cur_node = self.head
                self.head = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        node = HashLinkList.Node(obj)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for item in self:
            if item == obj:
                return True
            else:
                return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return '-->'.join(map(str, self))
'''


class OpenAddrHashTable:
    def __init__(self):
        self.size = 11
        self.skip = 3
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + self.skip) % self.size

    def __put(self, key, data):
        hash_value = self.hash_function(key)
        while self.slots[hash_value] is not None and self.slots[hash_value] is not key:
            hash_value = self.rehash(hash_value)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data

    def __get(self, key):
        hash_value = self.hash_function(key)
        start = hash_value
        data = None
        while self.slots[hash_value] is not None:
            if self.slots[hash_value] == key:
                data = self.data[hash_value]
                break
            else:
                hash_value = self.rehash(hash_value)
                if hash_value == start:
                    break
        return data

    def __getitem__(self, key):
        return self.__get(key)

    def __setitem__(self, key, value):
        self.__put(key, value)


class ZipperHashTable:
    def __init__(self, size=11):
        self.size = size
        self.slots = [HashLinkList() for _ in range(self.size)]

    def __set(self, key, val):
        hash_idx = self.__hash(key)
        self.slots[hash_idx].append(key, val)

    def __delitem__(self, key):
        hash_idx = self.__hash(key)
        self.slots[hash_idx].__delitem__(key)

    def extend(self, iterable=None):
        for item in iterable:
            self.__set(*item)

    def __contains__(self, key):
        hash_idx = self.__hash(key)
        if key in self.slots[hash_idx]:
            return True
        return False

    def keys(self):
        keys = []
        for item in self.slots:
            keys += item.keys()
        return keys

    def values(self):
        values = []
        for item in self.slots:
            values += item.values()
        return values

    def items(self):
        items = []
        for item in self.slots:
            items += item.items()
        return items

    def __get(self, key):
        hash_idx = self.__hash(key)
        if key in self.slots[hash_idx]:
            return self.slots[hash_idx][key]
        return None

    def __hash(self, key):
        return key % self.size

    def __repr__(self):
        return str(self.slots)

    def __getitem__(self, key):
        return self.__get(key)

    def __setitem__(self, key, value):
        self.__set(key, value)


class HashLinkList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, key, val):
        node = HashLinkList.Node(key=key, val=val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def extend(self, iterable):
        for obj in iterable:
            self.append(*obj)

    def __contains__(self, obj):
        for key, val in self:
            if key == obj:
                return True
        return False

    def __getitem__(self, obj):
        for key, val in self:
            if key == obj:
                return val
        return None

    def keys(self):
        keys = []
        for key, val in self:
            keys.append(key)
        return keys

    def __delitem__(self, key):
        prev = self.head
        cur = self.head.next
        if prev.key == key:
            self.head = cur
            return
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        raise KeyError

    def values(self):
        values = []
        for key, val in self:
            values.append(val)
        return values

    def __iter__(self):
        self.cur_node = self.head
        return self

    def __next__(self):
        if self.cur_node:
            node = self.cur_node
            self.cur_node = node.next
            return node.key, node.val
        else:
            self.cur_node = self.head
            raise StopIteration

    def __repr__(self):
        return '-->'.join(map(str, self))

    def items(self):
        return list(self)

    class Node:
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val
            self.next = None


if __name__ == '__main__':
    '''
    ht = OpenAddrHashTable()
    ht[0] = 'A'
    ht[1] = 'C'
    ht[3] = 'D'
    ht[4] = 'F'
    ht[12] = 'H'
    ht[10] = 'G'
    ht[2] = 'K'
    print(ht.slots)
    print(ht.data)
    print(ht[2])
    '''
    # lk = HashLinkList([(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (101, 'F')])
    # print(lk)
    # # print(lk)
    # # print(lk)
    # # print(isinstance(lk, Iterator))
    # print(0 in lk)
    # del lk[3]
    # print(lk)

    ht = ZipperHashTable()
    ht.extend([(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (101, 'F')])
    ht[13] = 'E'
    # ht.put(0, 'A')
    # ht.put(1, 'B')
    # ht.put(2, 'C')
    # ht.put(3, 'D')
    # ht.put(101, 'F')
    print(ht.items())
    print(ht[2])
    print(ht.keys())
    print(ht.values())
    print(ht.slots)
    del ht[1]
    print(ht.keys())
    print(ht.values())
    print(ht.slots)