

# В этой задаче нужно придумать генератор — однострочное выражение на языке Python, результатом вычисления которого будет двумерный массив (список вложенных списков), заполненный по некоторому правилу.
#

[[
    1 if j & 2 == 2 and i & 2 == 2 or j & 2 == 0 and i & 2 == 0 else 0
    for j in range(m)
] for i in range(n)]
