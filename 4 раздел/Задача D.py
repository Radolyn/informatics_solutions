# По данному натуральном \(n\) вычислите сумму 
# \(1^2+2^2+3^2+...+n^2\).
#    

n = int(input())
s = 0
for i in range(n + 1):
    s = s + i * i
print(s)
