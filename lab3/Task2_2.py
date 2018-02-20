import matplotlib.pyplot as plt
import numpy as np
x = np.arange(2, 4, 0.01)
y = [i * 3 + 0.01 for i in x]
plt.plot(x, y, 'b')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Sample graph')
plt.show()