steep = True
print("Вычисление квадратного корня")
try:
    a = float(input("Введите число: "))
    b = 3
    while steep:
        znach1 = (1/2)*(b + (a/b))
        b = znach1
    
        x = pow(a, .5)
        if znach1 == x:
            print("Ответ: ",znach1)
            steep = False
except ValueError:
    print("Вы ввели не значение")


