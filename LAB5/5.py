import numpy as np
mass = np.arange(50)
print(mass)
z = np.random.uniform(0,50)
print(z)
index = (np.abs(mass-z)).argmin()
print(mass[index])
