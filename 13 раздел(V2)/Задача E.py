# # 		Для данного символа, считанного со стандартного ввода, проверьте, является ли он цифрой. Решение оформите в виде функции IsDigit(c), возвращающей значение типа bool. В решении нельзя использовать циклы. В решении нельзя использовать константы с неочевидным значением типа 48 или 57.#     

a = input()


def IsDigit(c):
    if c.isdigit() == True:
        return 'YES'
    else:
        return 'NO'


print(IsDigit(a))