# Квадрат трехзначного числа оканчивается тремя цифрами, равными этому числу. Найдите и выведите все 
# такие числа.

for i in range(100, 1000):
    if i**2 % 1000 == i:
        print(i)
