# Оператор if

# number = 23
# guess = int(input('Введите целое число: '))

# if guess == number:
#     print('Поздравляем, вы угадали, ') # Здесь начинается новый блок
#     print('(хотя и не выйграли никакого приза!)') # Здесь заканчичвается новый блок
# elif guess < number:
#     print('Нет, загаданное число немного больше!') # Ёще один блок
#     # Внутри блока можно выполнять все что угодно
# else:
#     print('Нет, загаданное число немного меньше!')
#     # Чтобы попасть сюда, guess должно быть больше, чем number

# print('Завершено')
# Это последнее выражение выполняется всегда после выполнения операции if

# Оператор цикла while

# number = 23
# running = True

# while running:
#     guess = int(input('Введите целое число :'))

#     if guess == number:
#         print('Поздравляю, вы угадали!')
#         running = False # Это останавливает цикл while
#     elif guess < number:
#         print('Загаданное число немного больше.')
#     else:
#         print('Загаданное число немного меньше.')
# else:
#     print('Цикл while закончен.')
#     # Здесь можно выполнить все что угодно(в рамках разумного, конечно)
# print('Завершение')

# Оператор for

# for i in range(1, 10):
#     print(i)
# else:
#     print("Цикл for закончен")

# Оператор break

# while True:
#     s = input('Введите что-нибудь: ')
#     if s == 'выход':
#         break
#     print('Длинна строки: ', len(s))
# print('Завершение')

# Оператор continue

while True:
    s = input('Введите что-нибудь: ')
    if s == 'выход':
        break
    if len(s) <= 5:
        print('слишком мало')
        continue
    print('Введённая строка достаточной длины.')
    # Разные другие действия здесь ...



