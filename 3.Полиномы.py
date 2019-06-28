# python 3.Полиномы --znach 1 2 3 ....
import argparse as arg
import sys

otvet = 0
try:
    def createParser ():
        parser = arg.ArgumentParser()
        parser.add_argument('-z','--znach',nargs = '+', type=float)

        return parser

    print("Полиномы")
    print ("-------------------------------------------------")
    print("Ответы решения по формуле:")

    if __name__ == '__main__':
        parser = createParser()
        namespace = parser.parse_args(sys.argv[1:])

        for znach in namespace.znach:
            otv = 1/znach * 3
            print(znach, " = ",otv)
            otvet += otv
except ZeroDivisionError:
    print("[ERROR]: Вы ввели 0")
print ("-------------------------------------------------")
print ("Сумма равна:", otvet)
    

        
