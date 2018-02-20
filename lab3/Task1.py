q = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
w = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

def printM(a):
    for i in range(len(a)):
        print(a[i])

#Функция умножения на число
def umnoznaChislo(a,x = int(input(print("Введите число на которое надо умножить")))):
    for i in range(len(a)):
     for j in range(len(a)):
        a[i][j]*=x
    return printM(a)


#Функция сложения двух матриц
def plus(a,b):
    for i in range(len(a)):
        for j in range(len(a)):
           a[i][j]+= b[i][j]
    return printM(a)

#Функция транспонированной матрицы
def transpose(a):
    for i in range(len(a)):
     for j in range(0,i):
         tmp = a[i][j]
         a[i][j]=a[j][i]
         a[j][i]=tmp
    return printM(a)

#Функция умножения двух матриц
def matrixmult(m1,m2):
    s=0     #сумма
    t=[]    #временная матрица
    m3=[] # конечная матрица
    if len(m2)!=len(m1[0]):
        print("Матрицы не могут быть перемножены")
    else:
        r1=len(m1) #количество строк в первой матрице
        c1=len(m1[0]) #Количество столбцов в 1
        r2=c1           #и строк во 2ой матрице
        c2=len(m2[0])  # количество столбцов во 2ой матрице
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                   s=s+m1[z][i]*m2[i][j]
                t.append(s)
                s=0
            m3.append(t)
            t=[]
    return printM(m3)

print("Результат умножения на число")
umnoznaChislo(q)
print("Результат сложения двух матриц")
plus(q,w)
print("Транспонированная матрица")
transpose(q)
print("Результат умножения двух матриц")
matrixmult(q,w)



