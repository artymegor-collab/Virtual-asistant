import random
import datetime
import json




List = ["Камень-Ножницы-Бумага","Угадай число", "Узнать дату","Кто хочет стать миллионером", "Заметки", "Сгенерировать случайный пароль"]
true_login = "Агент001"
true_password = "12322"
login = input("Введите логин:")
user =  input("Введите пароль:")
while login != true_login or user != true_password:
    print("Неверный логин или пароль")
    login = input("Введите логин:")
    user =  input("Введите пароль:")
else:
    print("Вход выполнен")
    print("Привет, я твой виртуальный помощник")
    print("Можем поиграть или могу подсказать время")

    print(f"1 - {List[0]} \n 2 - {List[1]} \n 3 - {List[2]} \n 4 - {List[3]} \n 5 - {List[4]} \n 6 - {List[5]}")
user = int(input("Выберете (Введите число от 1 до 6): "))
if user == 1:
    List1 = ["Камень", "Ножницы", "Бумага"]
    print("Добро пожаловать в игру Камень-Ножницы-Бумага")
    print("Выберите один из вариантов:")
    print(f"1 - {List1[0]}  \n 2 - {List1[1]} \n 3 - {List1[2]}")
    user = int(input("Ваш выбор (Введите число от 1 до 5): "))
    user = List1[user - 1]
    print("Ваш выбор:" + user)
    bot = random.randint(1, 3)
    bot = List1[bot - 1]
    print("Выбор бота:" + bot)
    if user == bot:
        print("Ничья")
    elif (user == "Камень" and bot == "Ножницы") or (user == "Ножницы" and bot == "Бумага") or (
            user == "Бумага" and bot == "Камень"):
        print("Победа!")
    else:
        print("Проигрыш :(")
if user == 2:
    number = random.randint(1, 100)
    lives = 5
    while True:
        lives -= 1
        if lives == 0:
            print("ты проиграл, я загадал", number)
            break
        gues = int(input("Угадай число от 1 до 100"))
        if gues > number:
            print("Слишком большое число, попробуй ещё раз")
        elif gues < number:
            print("Слишком маленькое число, попробуй ещё раз")
        else:
            print("Поздравляю ты угадал!!!")
            break
if user == 3:
    date_time = datetime.datetime.now()
    print("Текущее время:", date_time.time())
    print("Сегодняшнее число", date_time.date())

if user == 4:
    money = 0
    lvl = 1

    correct_answers = {
        "Как называется самая высокая горная вершина Земли?": "A",
        "Какая столица Нидерландов?": "A",
        "Кто написал роман 'Война и мир'?": "B",
        "Когда распался советский союз?": "C"
    }

    questions = {
        "Как называется самая высокая горная вершина Земли?": {
            'A': 'Маунт-Эверест',
            'B': 'Канченджанга',
            'C': 'Килиманджаро',
            'D': 'Макалу'
        },
        "Какая столица Нидерландов?": {
            'A': 'Амстердам',
            'B': 'Гаага',
            'C': 'Утрехт',
            'D': 'Роттердам'
        },
        "Кто написал роман 'Война и мир'?": {
            'A': 'Александр Пушкин',
            'B': 'Лев Толстой',
            'C': 'Иван Тургенев',
            'D': 'Фёдор Достоевский'
        },
        "Когда распался советский союз?": {
            "A": "1980",
            "B": "1999",
            "C": "1991",
            "D": "1986"
        }}

    for question, answers in questions.items():
        print(question)
        for num, ans in answers.items():
            print(f'{num}: {ans}')
        answer = input('Твой ответ: ')
        if answer == correct_answers[question]:
            print('Правильный ответ')
            money += 100000 * lvl
            print(f'Заработано: {money}')
        else:
            print('Ответ неверный')
            break
        lvl += 1

if user == 5:
    notes = dict()


    def save_notes():
        with open("notes.json", "w") as file:
            json.dump(notes, file)


    def update_notes():
        global notes
        with open("notes.json", "r") as file:
            notes = json.load(file)


    def add_note(title, text):
        global notes
        notes[title] = text
        print("Заметка успешно добавлена")


    def display_notes():
        update_notes()
        if len(notes) == 0:
            print("Заметок пока нет")
        else:
            for title, text in notes.items():
                print(f"{title}: {text}")


    def delete_note(title):
        if title in notes.keys():
            del notes[title]
            print(f'Запись {title} удалена')
        else:
            print('Записи не существует')


    def main():
        while True:
            print("1 - добавить заметку")
            print("2 - посмотреть все заметки")
            print("3 - удалить заметку")
            print("4 - выйти")
            choice = input("Выберете действие:")
            if choice == "1":
                note_title = input("Введите название заметки: ")
                note_text = input("Введите текст заметки: ")
                add_note(note_title, note_text)
                save_notes()
            elif choice == "2":
                display_notes()
            elif choice == "3":
                update_notes()
                for title in notes.keys():
                    print(title)
                title_to_del = input('Введи название заметки для удаления: ')
                delete_note(title_to_del)
                save_notes()
            elif choice == "4":
                break
            else:
                print("Некорекктный ввод. Повторите попытку.")


    main()

random_password = ['1', '2', '3', '4', '5', 'g', 'h', 'b', '$', 'L','F','_','M','-']
password = ''
if user == 6:
    a = int(input('Введите длину пароля '))
    for i in range(a):

        password +=(random.choice(random_password))
    print(password)


