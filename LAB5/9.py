import numpy as np
mass = np.random.randint(0,10,10)
print(mass)
print(np.bincount(mass).argmax())
