import random

print(' - Вывод случайного числа при помощи использования random.random()')
print(random.random())

from random import randint, randrange

print(" - Вывод случайного целого числа ", randint(0, 9))
print(" - Вывод случайного целого числа ", randrange(0, 10, 2))

city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print(" - Выбор случайного города из списка - ", random.choice(city_list))

print(" - Использование random.randint() для генерации случайного целого числа")
print(random.randint(0, 5))
print(random.randint(0, 5))

print(" - Генерация случайного числа в пределах заданного промежутка")
print(random.randrange(10, 50))
print(random.randrange(10, 50, 5))

list = [55, 66, 77, 88, 99]
print(" - random.choice используется для выбора случайного элемента из списка - ", random.choice(list))

list = [2, 5, 8, 9, 12]
print (" - random.sample() ", random.sample(list,4))

list = [20, 30, 40, 50 ,60, 70, 80, 90]
sampling = random.choices(list, k=5)
 
print(" - Выборка с методом choices ", sampling)

random.seed(6)
print(" - Случайное число с семенем ",random.random())
 
print(" - Случайное число с семенем ",random.random())

list = [8, 3, 5, 1, 6, 2]

random.shuffle(list)
print(" - Вывод перемешаного списка ", list)

print(" - Число с плавающей точкой в пределах заданного промежутка ")
print(random.uniform(10.5, 25.5))

print(" - Число с плавающей точкой через triangular")
print(random.triangular(10.5, 25.5, 5.5))


