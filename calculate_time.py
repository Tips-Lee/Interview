import time


class cal_time:
    def __init__(self, func):
        self.f = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        ans = self.f(*args, **kwargs)
        end = time.time()
        t = end - start
        print('total time: %f' % t)
        return ans