x = 1
y = 2
def call(a, b):
    return a + b

call_cell = lambda : call(x, y)

print(call_cell())