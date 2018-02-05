num = input()
a = [int(i) for i in str(num)]
for i in range(0,len(a), 1):
  if i%2 == 0:
    print(a[i])