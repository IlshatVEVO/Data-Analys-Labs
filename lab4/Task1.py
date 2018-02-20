import random
import matplotlib as lib
import matplotlib.pyplot as plot

moneta = []

for i in range(1, 1001):
    rand = random.randint(1, 100)
    if (rand >= 30):
        moneta.append(0)
    else:
        moneta.append(1)

labels = ['Reshka', 'Orel']
values = [0] * 2

for i in range(len(moneta)):
    if (moneta[i] == 0):
        values[0] += 1
    else:
        values[1] += 1

figure1, ax1 = plot.subplots()
ax1.pie(values, labels = labels,
        autopct = '%1.1f%%', startangle = 90)
ax1.axis('equal')
plot.show()
