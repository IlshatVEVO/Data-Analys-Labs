#Дана случайная матрица. Вычтите среднее значение для каждой строки матрицы.
import numpy as np
a = np.random.randint(10, size=(5,5))
print(a)
sum = int(0)
for i in range(len(a)):
    for j in range(len(a)):
        sum +=a[i][j]
    print(sum/len(a))

