import numpy as np
import matplotlib.pyplot as plt
import math


def present_value(irr, period, pmt=1., fv=0):
    def _one_period_flow(i, int_rate, pmt):
        return pmt/np.power((1 + int_rate), i)
    ans = 0
    for i in range(1, period+1):
        ans += _one_period_flow(i, irr, pmt)

    return ans + _one_period_flow(period, irr, fv)


def train():
    irr = 0.12
    fv = 0
    period = 12
    fee = 0.0075
    pmt = 1. / 12 + fee
    eps = 0.000001
    loss = -1 + present_value(irr, period, pmt, fv)
    while np.abs(loss) > eps * 4:
        if loss > 0:
            irr = irr + eps
            loss = -1 + present_value(irr, period, pmt, fv)
        else:
            irr = irr - eps
            loss = -1 + present_value(irr, period, pmt, fv)
    final_irr = np.power((irr + 1), period)
    print('Final IRR: {:.6f}'.format(final_irr))


def irr_plot():
    def _plot(irr, loss):
        plt.figure(figsize=(4,4))
        plt.plot(irr, loss)
        plt.show()

    irr = np.linspace(0, .02, 100)
    fv = 0
    pv = -1
    period = 12
    fee = 0.0075
    pmt = 1. / 12 + fee
    loss = pv + present_value(irr, period, pmt, fv)
    irr = np.power((1 + irr), period) - 1
    _plot(irr, loss)


if __name__ == '__main__':
    train()
    irr_plot()