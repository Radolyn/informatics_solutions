# Во входном файле записано два целых числа, которые могут быть разделены пробелами и концами строк. Выведите в выходной файл их сумму. 
f = open('input.txt')
s = f.readlines()
s = "".join(s)
s = s.split()
a = 0
for i in s:
    a += int(i)
print(a)
f.close()
