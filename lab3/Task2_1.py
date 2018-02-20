import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 50, 0.01)
y = [i * 2.9 + 10 for i in x]
plt.plot(x, y, 'b')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Draw line')
plt.show()