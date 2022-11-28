# Напишите программу, которая принимает на вход 2 числа,
# и проверяет являится ли одно число квадратом другого.
# Например:
# 5, 25 -> Да
# 4, 16 -> Да
# 25, 5 -> Да
# 8, 9 -> Да

# Первый вариант решения:

# def is_square_namber(first_num, sec_num, start = 1):
   # while start < sec_num:
     #   start *= first_num
    # print(start)
    # if (start == sec_num):
    #    return True
    # else: 
     #   return False
# print(is_square_namber(int(input('Введите первое число: ')), int(input('Введите второе число: '))))

# Второе решение

num1 = int (input('Введите первое число: '))
num2 = int (input('Введите второе число: '))
if num2**2 == num1 or num1**2 == num2:
    print ('Да')
else:
    print ('Нет')