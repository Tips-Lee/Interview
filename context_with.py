import contextlib


class A:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import traceback
        print(self, exc_type, exc_val)
        print('exit')
        print(traceback.extract_tb(exc_tb))
        return True


@contextlib.contextmanager
def cm():
    try:
        yield
    except LessZero as e:
        print(e)


class cm2:
    def play(self):
        print('play')

    def close(self):
        print('close')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return True


class LessZero(Exception):
    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.error_code = kwargs['error_code']

    def __str__(self):
        return str(self.name) + '\t Error Code:' + str(self.error_code)


class Person:
    def __init__(self, name, age):
        self.name = name
        # age/0
        if age < 0:
            raise LessZero('less than zero !!', error_code=444)
        self.age = age

try:
    p = Person('lily', -18)
except LessZero as e:
    print(e, type(e))