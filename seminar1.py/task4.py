# Напишите программу, которая на вход будет принимать дробь и показывать первую цифру дробной части.

# Первый вариант решения задачи

import math # Вывод функции из библиотеки

num = float(input('Введите дробное число: '))
# print(int(num * 10) %10)
print(math.floor(num * 10) %10)

# Второй вариант решения задачи

# num = input('Введите дробное число: ')
# numbers = num.split('.')
# if len (numbers) == 1:
#     print ('Нет')
# else:
#     num = numbers[1]
#     print(num[:1])

