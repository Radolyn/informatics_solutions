# Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k,
# сдвинув влево все элементы, стоящие правее элемента с индексом k.
# 



l = list(map(int, input().split()))
num = int(input())

del l[num]

for i in range(len(l)):
    print(l[i], end=' ')