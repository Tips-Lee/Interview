import win32com.client
speaker = win32com.client.Dispatch('SAPI.SpVoice')
speaker.Speak('你好！')

class Calculator:

    def __get_voice(operation=''):
        def __voice_decorator(func):
            def inner(self, num):
                print('Speak--- %s %d' % (operation, num))
                return func(self, num)
            return inner
        return __voice_decorator

    def __check_decorator(func):
        def inner(self, num):
            if not isinstance(num, int):
                raise TypeError('wrong type, only support int type')
            return func(self, num)
        return inner

    @__check_decorator
    @__get_voice()
    def __init__(self, num):
        self.v = num

    @__check_decorator
    @__get_voice('add')
    def add(self, num):
        self.v += num
        return self

    @__check_decorator
    @__get_voice('sub')
    def sub(self, num):
        self.v -= num
        return self

    @__check_decorator
    @__get_voice('mul')
    def mul(self, num):
        self.v *= num
        return self

    def show(self):
        print('Speak--- %s %d' % ('最终结果是', self.v))
        print('最终结果是：%s' % self.v)

num = Calculator(2)
num.add(3).sub(1).mul(5).show()
# (2+3-1)*5