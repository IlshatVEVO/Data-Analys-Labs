#Вам дан текст на английском языке, посчитайте частоту встречаемости каждой буквы,
#не учитывайте все другие знаки препинания и пробел (буквы только a-z).
#Покажите наглядно на графике.
import matplotlib as mpl
import matplotlib.pyplot as plt

data = []
abcd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mess = "hello, my friend. how do you do?"

for i in range(len(abcd)):
    count = 0
    for j in mess:
        if (j == abcd[i]):
                count += 1
    data.append(count)
    print("%s - %s" % (abcd[i], count))
print(data)
print(len(data))

dpi = 100
fig = plt.figure(dpi = dpi, figsize = (600 / dpi, 400 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.title('hello, my friend. how do you do?')

ax = plt.axes()

xs = range(len(abcd))
plt.bar([x + 0.0 for x in xs],  data,
          color = 'blue', alpha = 0.8,
         zorder = 0)
plt.xticks(xs, abcd, rotation =10)
plt.show()

