password = "123456"
user = input("Введи пароль:")
if user == password:
    print("Вход выполнен")
if user != password:
    print("Неверный пароль")
if user == password:
    input("Привет Егор. чем могу помочь?")
    import datetime
    date_time = datetime.datetime.now()
    print("Текущее время:", date_time.time())
    print("Сегодняшнее число", date_time.date())