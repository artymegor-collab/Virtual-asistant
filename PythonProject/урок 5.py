import random
List = [ "Камень", "Ножницы" , "Бумага" ]
print("Добро пожаловать в игру Камень-Ножницы-Бумага")
print("Выберите один из вариантов:")
print(f"1 - {List[0]}  \n 2 - {List[1]} \n 3 - {List[2]}")
user = int(input("Ваш выбор (Введите число от 1 до 3): "))
user = List[user - 1]
print("Ваш выбор:" + user )
bot = random.randint (1,3)
bot = List[bot - 1]
print("Выбор бота:" + bot )
if user == bot:
    print("Ничья")
elif (user == "Камень" and bot == "Ножницы" ) or(user == "Ножницы" and bot == "Бумага") or(user == "Бумага" and bot == "Камень") :
    print("Победа!")
else:
    print("Проигрыш :(")