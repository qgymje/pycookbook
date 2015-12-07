import numpy as np

ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])

print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

def f(x):
    return 3*x**2 - 2*x +7

print(f(ax))
print(np.sqrt(ax))
print(np.cos(ax))
