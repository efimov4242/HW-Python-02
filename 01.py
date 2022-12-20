# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def getSumNumb(numb):
	sum = 0
	if numb == int(numb):
		while (0 < numb):
			sum += int(numb) % 10
			numb /= 10
		return int(sum)
	else:
		for char in str(numb):
			if char != '.':
				sum += int(char)
		return sum

print(getSumNumb(232))
