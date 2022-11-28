# Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять колличество вхождений в одной строки в другой.

str1 = input('первая строка: ')
str2 = input('вторая строка: ')
# второй вариант str1, str2 = input('первая строка: '), input('вторая строка: ')
# третий вариант str1, str2 = input('первая строка: ').lower(), input('вторая строка: ').lower()

count = 0
str1 = str1.split()
for i in str1:
    if i == str2:
        count +=1
print(count)

# Третий вариант

str1, str2 = input('первая строка: ').lower(), input('вторая строка: ').lower()
str1.replace(',', '')
count = 0
str1 = str1.split()
print(str1)
for i in str1:
    if i == str2:
        count +=1
print(count)

# Четвертый вариант
print(str1.count(str2))
