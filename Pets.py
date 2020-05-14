class Animal:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def sleep(self):
        print('%s 在睡觉' % self)

    def eat(self):
        print('%s 在吃饭' % self)

    def __str__(self):
        return '名字%s, 年龄%d'%(self.name, self.age)


class Dog(Animal):
    def __init__(self, name, age=1):
        super(Dog, self).__init__(name, age)

    def work(self):
        print('%s 在看家' % self)

    def __str__(self):
        return '名字%s, 年龄%d 的小狗' % (self.name, self.age)


f1 = open('test.html', 'r', encoding='utf-8')
f2 = f1.__enter__()
f3 = f2.readlines()
print(f3[0])
f2.__exit__(BaseException, BaseException,)