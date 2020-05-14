import datetime
from functools import partial, total_ordering
from collections import Iterator, Iterable

class Weight:
    def __get__(self, instance, owner):
        # print('get', self, instance, owner)
        return instance.value

    def __set__(self, instance, value):
        # print('set', instance, value)
        instance.value = value

    def __delete__(self, instance):
        print('delete')


@total_ordering
class Person:
    def __init__(self, age, height, li=None):
        self.cache = li
        self.__age = age
        self.height = height
        self.count = 0

    weight = Weight()

    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, value):
    #     self.__age = value
    #
    # @age.deleter
    # def age(self):
    #     del self.__age

    # age = property(get_age, set_age, del_age, 'age property')

    def __setitem__(self, key, value):
        # print('setitem')
        self.cache[key] = value

    # def __getitem__(self, item):
    #     if self.cache[item]:
    #         return self.cache[item]
    #     else:
    #         return 'No item'

    # def __getitem__(self, item):
    #     print('getitme')
    #     self.count += 1
    #     if self.count > 5:
    #         raise StopIteration('stop iter')
    #     return self.count

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        # print('iter')
        self.count += 1
        if self.count > 4:
            raise StopIteration('stop iter')
        return self.count

    def __delitem__(self, key):
        del self.cache[key]

    def __eq__(self, other):
        print('==')
        return self.__age == other.age

    # def __ne__(self, other):
    #     print('!=')
    #     return self.age != other.age

    def __gt__(self, other):
        print('>')
        return self.__age > other.age

    # def __ge__(self, other):
    #     return self.age >= other.age
    #
    # def __lt__(self, other):
    #     return self.age < other.age
    #
    # def __le__(self, other):
    #     return self.age <= other.age

    def __bool__(self):
        return self.__age > 18

    def __call__(self, *args, **kwargs):
        self.count += 1
        if self.count > 4:
            raise StopIteration('stop iter')
        return self.count



if __name__ == '__main__':
    p1 = Person(19, 180)
    p2 = Person(17, 170)
    # print(p1 <= p2)
    # print(Person.__dict__)
    # pt = iter(p1)
    # print(p1.weight)
    p1.weight = 18
    print(p1.weight)
    # del p1.age
    # print(p1.age)
    # help(p1)
    # print(p2.weight)
    p2.weight = 19
    print(p2.weight)
    print(p1.weight)