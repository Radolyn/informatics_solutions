# Гипотеза Гольдбаха (недоказанная до сих пор) утверждает,
# что любое четное число (кроме 2) можно представить в виде
# суммы двух простых чисел. Дано натуральное четное число,
# большее 2, выведите два простых числа, дающих в сумме данное.



def isPrime(n):
    i = 2
    while n % i != 0:
        i += 1
        if i**2 > n:
            return True
    return False


n = int(input())

if n == 4:
    print(2, 2)

for i in range(2, n // 2 + 1, 1):
    if isPrime(i) and isPrime(n-i):
        print(i, n - i)
        break
