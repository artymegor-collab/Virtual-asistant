import datetime
List = ["Узнать время", "Таблица умножения"]
date_time = datetime.datetime.now()
print("Привет, чем могу помочь?")
print(f"1 - {List[0]} \n 2 - {List[1]}")
user = int(input("Выберете число от 1 до 2:"))
if user == 1:
    date_time = datetime.datetime.now()
    print("Текущее время:", date_time.time())
    print("Сегодняшнее число:", date_time.date())
elif user == 2:
    for num1 in range(1, 10):
        for num2 in range(1, 10):
            print(f"{num1} * {num2} = {num1 * num2}")
        print("----------")
