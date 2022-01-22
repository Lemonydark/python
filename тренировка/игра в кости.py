import random

PlayerOne = "Anna"
PlayerTwo = "Rita"

AnnaScore = 0
RitaScore = 0

# У каждого кубика шесть сторон
DiceOne = [1, 2, 3, 4, 5, 6]
DiceTwo = [1, 2, 3, 4, 5, 6]

def playDiceGame():
    """Оба участника, Anna и Rita, бросают кубик, используя метод shuffle"""

    for i in range(5):
        #оба кубика встряхиваются 5 раз
        random.shuffle(DiceOne)
        random.shuffle(DiceTwo)
    firstNumber = random.choice(DiceOne) # использование метода choice для выбора случайного значения
    secondNumber = random.choice(DiceTwo)
    return firstNumber + secondNumber

print("Игра в кости использует модуль Random\n")

# Давайте сыграем в кости три раза
for i in range(3):
    # Определим, кто будет бросать кости первым
    AnnaTossNumber = random.randint(1, 100) # генерация случайного числа от 1 до 100, включая 100
    RitaTossNumber = random.randrange(1, 101, 1) # генерация случайного числа от 1 до 100, не включая 101

    if(AnnaTossNumber > RitaTossNumber):
        print("Anna выйграла жеребьёвку.")
        AnnaScore = playDiceGame()
        RitaScore = playDiceGame()
    else:
        print("Rita выйграла жеребьёвку.")
        RitaScore = playDiceGame()
        AnnaScore = playDiceGame()

    if(AnnaScore > RitaScore):
        print("Anna выиграла игру в кости.\nФинальный счет Anna:", AnnaScore, "\nФинальный счет Rita:", RitaScore)
    elif(AnnaScore < RitaScore):
        print("Rita выиграла игру в кости.\nФинальный счет Rita:", RitaScore, "\nФинальный счет Anna:", AnnaScore)
    else:
        print("Ничья.\nФинальный счет Anna:", AnnaScore, "\nФинальный счет Rita:", RitaScore)
    
