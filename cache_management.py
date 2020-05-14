from sys import getrefcount
class Person:
    pass

p1 = Person()
print(getrefcount(p1))
p2 = p1
print(getrefcount(p2))
del p2
print(getrefcount(p1))
del p1