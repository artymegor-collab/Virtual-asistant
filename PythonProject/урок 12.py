import json

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




