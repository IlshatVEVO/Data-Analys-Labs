import numpy as np
N = int(input())
mass = np.random.randint(0,10,N)
print(mass)
mass[mass.argmax()] = 0
print(mass)
