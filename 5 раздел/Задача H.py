# Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
# Вклад составляет X рублей Y копеек. Определите размер вклада через год.


p = int(input())
x = int(input())
y = int(input())

mb = 100 * x + y
ma = int(mb * (100 + p) / 100)

print(ma // 100, ma % 100)
