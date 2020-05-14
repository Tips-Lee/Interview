
class Bio:
    pass

class Animal(object):
    # __slots__ = ()
    _name = 'tips'
    _age = 1


class Dog(Animal, Bio):
    __slots__ = ('eat', 'drink')
    pass

#
a = Animal()
# d = Dog()

