import random
print("Хочешь узнать немного больше о своем друге или близком человеке?")
freind_name = input("Введи его имя и я раскрою его тайны")
fake_news = [
    f" {freind_name.title()} обнаружен на мальдивах ",
    f"Шокирующее открытие: {freind_name.title()} оказался фараоном ",
    f" {freind_name.title()} признался в том что он вор",
    f" Испуганый {freind_name.title()} попал в другую галкатику",
    f" поразительное превращение: {freind_name.title()} оказался вампиром "
    ]
num = random.randint(0,len(fake_news) - 1 )
print(fake_news[num])

