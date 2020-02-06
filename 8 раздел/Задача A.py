# Даны четыре действительных числа: \(x_1\), \(y_1\), \(x_2\), \(y_2\). Напишите функцию
# distance(x1, y1, x2, y2), вычисляющую расстояние
# между точкой \((x_1,y_1)\) и \((x_2,y_2)\). Считайте четыре действительных числа
# и выведите результат работы этой функции.


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


print(distance(float(input()), float(input()), float(input()), float(input())))
