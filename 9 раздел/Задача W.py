# Дан список целых чисел. Требуется “сжать” его, переместив
# все ненулевые элементы в левую часть списка, не меняя их порядок, а все нули - в правую
# часть. Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
# задачу нужно выполнить за один проход по списку. Распечатайте полученный список.

l = list(map(int, input().split()))

c = l.count(0)

l = list(filter(lambda a: a != 0, l))

for i in range(c):
    l.append(0)

for item in l:
    print(item, end=' ')
