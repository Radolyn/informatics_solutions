# С начала суток часовая стрелка повернулась на угол в \(\alpha\) градусов. Определите
# на какой угол повернулась минутная стрелка с начала последнего часа.
# Входные и выходные данные — действительные числа.



import math

a = float(input())
print(a % 30 * 12)