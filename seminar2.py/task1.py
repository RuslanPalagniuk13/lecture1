# Напишите программу, которая принимает на вход число N и выдает последованность из N членов.
# Пример - для N = 5: 1, -3, 9, -27, 81

num = int(input('Введите число N: '))
res = 1
for i in range(1, num + 1):
    print(res, end = ', ')
    res *= -3
    
# for i in range(int(input())):
# print((-3)**i, end = ', ')