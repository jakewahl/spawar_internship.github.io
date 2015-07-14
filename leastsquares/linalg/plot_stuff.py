__author__ = 'jakewahl'

import matplotlib.pyplot as plt
import numpy as np

def least_squares(y, H):
    projection = np.dot(np.linalg.inv(np.dot(H.T, H)), H.T)
    u = np.dot(projection, y)
    s = np.dot(H, u)
    return s, u

x = np.linspace(0, 2, 40, False)
H = np.array([np.ones(x.shape), x]).T
H2 = np.array([np.ones(x.shape), x, x ** 2]).T
f = x ** 2 - 2 * x + 2
std = .3

e = std * np.random.randn(len(x))
y = f + e
s, est = least_squares(y, H)
s1, _ = least_squares(y, H2)
# plt.scatter(x, f)
m = plt.scatter(x, y, c="r", s=31, label="measurements")
gt = plt.plot(x, f, '-', c="k", linewidth=3, label="ground truth")
hat = plt.plot(x, s, 'o-', label="estimate")
hat2 = plt.plot(x, s1, 'o-', c="orange", label="better estimate")
plt.legend()
plt.show()

