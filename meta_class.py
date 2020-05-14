import inspect, abc


class Animal(object, metaclass=abc.ABCMeta):
    def __init__(self):
        self.age = 10

    # @abc.abstractmethod
    def f(self):
        print('af')

    @classmethod
    @abc.abstractmethod
    def f1(cls):
        print('af1')


class Dog(Animal):
    def __init__(self):
        self.name = 'teddy'
        super(Dog, self).__init__()

    def f(self):
        super(Dog, self).f()
        print('Dog')

    @classmethod
    def f1(cls):
        super(Dog, cls).f1()
        print('cls')

    @staticmethod
    def f2():
        print('static')

    def __str__(self):
        return 'str dog'

d = Dog()
print('%s'%(d))