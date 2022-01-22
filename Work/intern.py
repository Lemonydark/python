# Вывести квадрат числа
import random
import math

n = random.randint(1, 100)
print(n)
print(n ** 2)

# По двум заданным числам проверять является ли первое квадратом второго
a = 2
b = random.randint(1, 5)

if(b ** 0.5 == a):
    print(True)
else:
    print(False)

import math

c = [2, 3, 4, 5, 6, 7, 8, 9]
d = [4, 9, 16, 25, 36, 49, 64, 81]
N1 = random.shuffle(c)
N2 = random.shuffle(d)
M2 = math.sqrt(16)
if(M2 == N1):
    print(True)
else:
    print(False)

# Даны два числа. Показать большее и меньшее число

number1 = random.randint(1,10)
number2 = random.randint(1,10)
if(number1 > number2):
    print(number1, ' большее')
    print(number2, ' меньшее')
else:
    print(number1,'меньшее ')
    print(number2,'большее')

# По заданному номеру дня недели вывести его название

#d = int(input('Введите день недели: '))
#if(d == 1):
#    print('Понедельник')
#elif(d == 2):
#    print('Вторник')
#elif(d == 3):
#    print('Среда')
#elif(d == 4):
#    print('Четверг')
#elif(d == 5):
#    print('Пятница')
#elif(d == 6):
#   print('Суббота')
#elif(d == 7):
#   print('Воскресенье')
#else:
#    print('Ошибка')

#n60 = int(input('Введите день: '))
#res = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
#print(res[n60-1])

# Найти максимальное из трех чисел

i = 2
o = 8
p = 5

max = i
if(i > max):
    max = i
if(o > max):
    max = o
if(p > max):
    max = p

print(max)

# Написать программу вычисления значения функции y = f(a)
