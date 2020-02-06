# По данному натуральному n≥2 вычислите сумму
# 1×2+2×3+...+(n-1)×n. Ответ выведите в виде
# вычисленного выражение и его значения в точности, как показано в примере.
#    



n = int(input())
print("+".join("{}*{}".format(k, k + 1) for k in range(1, n)), end="=")
print(sum(k * (k + 1) for k in range(1, n)))