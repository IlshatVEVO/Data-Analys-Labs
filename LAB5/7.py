import numpy as np

a = np.random.randint(10, size=(5,5))
print(a)
b = np.random.randint(10, size=(5,5,3))
print(b)
c = a*b
print(c)
