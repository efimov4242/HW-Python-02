# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

import random

n = 5
lst = [random.randint(0, 10) for i in range(1, n+1)]
print(*lst)
for j in range(len(lst)-1):
	lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(*lst)