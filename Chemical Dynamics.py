import numpy as np
import matplotlib.pyplot as plt

A = 100
k_init = .1
x_lim = 365
def f1(t):
    k = k_init * 2
    ans = A - k*t
    return ans


def f2(t):
    k = 0.05 * k_init
    ans = A * np.exp(-k * t)
    return ans


def f3(t):
    k = 0.005 * k_init
    ans = 1/A + k*t
    return 1/ans

t = np.linspace(0, x_lim, 1000)
plt.plot(t, f1(t), label='Zero Order')
plt.plot(t, f2(t), label='First Order')
plt.plot(t, f3(t), label='Second Order')
plt.title('Chemical Reaction Dynamics')
plt.xlim(0, x_lim)
plt.ylim(0)
plt.xlabel('Time / Day')
plt.ylabel('Relative Concentration / %')
plt.legend()
plt.show()