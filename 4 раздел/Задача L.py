# Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.

n = 0
for i in range(10):
    number = int(input())
    n += number
print(n)
