# Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n флагов. Изображение одного флага
# имеет размер 4×4 символов, между двумя соседними флагами также имеется пустой (из пробелов) столбец. Разрешается
# вывести пустой столбец после последнего флага. Внутри каждого флага должен быть записан его номер — число от 1 до n.
#    



n = int(input())

a = '+___ '
b = '|__\\ '
c = '|    '


print(a * n)
for i in range(1, n + 1):
    print('|', i, ' / ', sep='', end='')
print()
print(b * n)
print(c * n)
