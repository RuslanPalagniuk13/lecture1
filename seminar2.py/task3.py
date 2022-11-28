# Первый вариант решения:

# n = int(input('Введите число n: '))
# dst = {}
# for i in range(1, n+1):
#    dst[i] = 3*i + 1
# print(dst)


# Второй вариант решения:

# dst = {}
# for i in range(1, int(input('Введите число n: '))+1):
#   dst[i] = 3*i + 1
# print(dst)


# Третий вариант решения:

dst = {i: 3*i + 1 for i in range(1, int(input('Введите число n: '))+1)}
print(dst)