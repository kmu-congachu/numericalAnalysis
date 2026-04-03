import numpy as np
import matplotlib.pyplot as plt


def incsearch(func, min, max, ns):
    x = np.linspace(min, max, ns)
    f = func(x)
    nb = 0
    xb = []
    for k in np.arange(np.size(x) - 1):
        if np.sign(f[k]) != np.sign(f[k + 1]):
            nb += 1
            xb.append([x[k], x[k + 1]])

    xb = np.round(xb, 2)
    return nb, xb


def draw(xmin, xmax, inc, func):
    x = np.linspace(xmin, xmax, inc)
    f1 = func(x)
    plt.figure(1)
    plt.plot(x, f1, 'ro-')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    x_min = 3
    x_max = 6
    inc = 100
    func = lambda x: np.sin(np.dot(10.0, x)) + np.cos(np.dot(3.0, x))
    nb, xb = incsearch(func, x_min, x_max, inc)
    draw(x_min, x_max, inc, func)
    print('number of brackets= ', nb)
    print('root interval=', xb)
