# Выведите в обратном порядке содержимое всего файла полностью. Для этого считайте файл целиком при помощи метода read().




file = open('input.txt', 'r')
array = file.read()
print(array[::-1])
