# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

l = list(map(int, input().split()))

for item in l:
    if l.count(item) == 1:
        print(item, end=' ')
