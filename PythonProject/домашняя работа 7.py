import random
number = random.randint(1, 350 )
lives = 5
while True:
    lives -= 1
    if lives == 0:
        print("ты проиграл, я загадал число ", number )
        break
    gues = int(input("Угадай число от 1 до 100"))
    if gues > number:
        print("Слишком большое число, попробуй ещё раз")
    elif gues < number:
        print("Слишком маленькое число, попробуй ещё раз")
    else:
        print("Поздравляю ты угадал!!!")
        break