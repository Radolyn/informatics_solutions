# Дана строка. Если в этом числе буква f встречается
# только один раз, выведите её индекс. Если она встречается два и более раз,
# выведите индекс её первого и последнего появления. Если буква
# f в данной строке не встречается, ничего не выводите.


text = input()

first = text.find('f')
second = text.rfind('f')

if first == -1:
    pass
elif first == second:
    print(first)
else:
    print(first, second)
