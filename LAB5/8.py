import numpy as np
mass = np.random.uniform(0,10,(5,5))
print(mass)
rank = np.linalg.matrix_rank(mass)
print(rank)
