# Возведение в степень
print(2 ** 4)

num1 = 2
num2 = -5
num3 = 0
num4 = 1.025
num5 = 0.5

print(num1,'^12 =',num1 ** 12)
print(num2,'^4 =',num2 ** 4)
print(num3,'^99999 =',num3 ** 99999)
print(num4,'^-3 =',num4 ** -3)
print(num5,'^8 =',num5 ** 8)

import math

print(pow(6, 2)) # pow будет работать без ввода команды import math
print(math.pow(5, 2))

# Корень
num = 25
sqrt = num ** (0.5)
print("Квадратный корень из числа "+ str(num) +" это "+str(sqrt))

# Использование math.sqrt()
import math

Num = 25
sqrt1 = math.sqrt(Num)
print("Квадратный корень из числа " + str(Num) + " это " + str(sqrt1))

Num1 = 0
sqrt2 = math.sqrt(Num1)
print("Квадратный корень из числа " + str(Num1) + " это " + str(sqrt2))

# Использование отрицательного числа
import cmath
NUM = -25
SQRT = cmath.sqrt(NUM)
print("Квадратный корень из числа " + str(NUM) + " это " + str(SQRT))

# Использование комплексного числа в качестве аргумента
num9 = 4 + 9j
sqrt9 = cmath.sqrt(num9)
print("Квадратный корень из числа " + str(num9) + " это " + str(sqrt9))

