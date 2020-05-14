import objgraph, gc, weakref
gc.disable()

class Person:
    def __del__(self):
        print('person clear')


class Dog:
    def __del__(self):
        print('dog clear')


p = Person()
d = Dog()
p.pet = weakref.ref(d)
d.master = weakref.ref(p)
print(objgraph.count('Person'))
print(objgraph.count('Dog'))

del p
del d

# gc.collect()
print(objgraph.count('Person'))
print(objgraph.count('Dog'))

# weakref.WeakKeyDictionary()
