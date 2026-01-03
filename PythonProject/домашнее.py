import random
input("Я магический шар, ты хочешь узнать что тебя сегодня ждёт?")
name = input("Что бы узнать предсказание скажи, как тебя зовут?")
prediction = [
    f"Сегондня {name.title()} получит удачу ",
    f"Сегодня {name.title()} найдет денги",
    f" {name.title()} сегодня тебя машина обольет водой",
    f"Сегодня {name.title()} получит 5 по английскому "
    f"Сегодня {name.title()} хорошо погуляет  "]
num = random.randint(0,len(prediction) - 1 )
print(prediction[num])

