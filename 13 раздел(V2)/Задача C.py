# 
# 		Выведите все символы ASCII с кодами от 33 до 126 и их коды в следующем виде:
# символ код
#     

for i in range(33, 127):
    print(chr(i) + ' ' + str(i), end='\n')
