a, b = [int(input()) for i in range(2)]

even = a + a % 2
for i in range(even, b + 1, 2):
    print(i, end=' ')