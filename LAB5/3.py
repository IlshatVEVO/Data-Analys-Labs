import numpy as np
mass = np.arange(11)
print(mass)
mass[(3 < mass) & (mass <= 10)] *= -1
print(mass)
