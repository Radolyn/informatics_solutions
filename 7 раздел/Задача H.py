# Программа получает на вход последовательность целых неотрицательных чисел,
# каждое число записано в отдельной строке. Последовательность завершается числом
# 0, при считывании которого программа должна закончить свою работу и вывести
# количество членов последовательности (не считая завершающего числа 0).
# 


a = 0
b = 0

s = True


def calc(a, b):
    print(a / b)
    exit()


while s:
    n = int(input())

    if n == 0:
        print(b)
        break

    b += 1
