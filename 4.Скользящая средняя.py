from random import randint
a = []
N = int(input("Введите количество значений: "))
S = int(input("Введите значение шага: "))
k = 0
summ1 = 0
steep = S
for i in range(N):
    a.append(randint(1,99))
    
print(a)

while k < N:
    try:
        while k < S:
            summ1 += a[k]
            k += 1
    except IndexError:
        break
    summ1 = summ1 / 3
    print(summ1)
    summ1 = 0
    print("-----------------------")
    S += steep
    
        
