# 
# 		В таблице из $N$ строк и $N$ столбцов некоторые клетки заняты шариками, другие свободны. Выбран шарик, который нужно переместить, и место, куда его нужно переместить. Выбранный шарик за один шаг перемещается в соседнюю по горизонтали или вертикали свободную клетку. Требуется выяснить, возможно ли переместить шарик из начальной клетки в заданную, и если возможно, то найти путь из наименьшего количества шагов. 
#     

text = input()

text1 = text[:text.find('h')]

text2 = text[text.find('h'):text.rfind('h') + 1]

text3 = text[text.rfind('h') + 1:]

text = text1 + text2[::-1] + text3  # reverse + add left & right positions

print(text)
