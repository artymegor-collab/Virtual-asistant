import random
import time
print("Добро пожаловать в игру Орёл и Решка")
print("Выбери один из вариантов: \n 1 - Орёл \n 2 - Решка")
user = int(input("(Ваш выбор: Выберите число от 1 до 2):"))
time.sleep(1)
bot = random.randint (1, 2)
if user == bot:
    print("ничья")
else:
    print("проигрыш")

