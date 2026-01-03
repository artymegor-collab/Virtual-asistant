true_password = "12322"
user =  input("Введите пароль:")
while user != true_password:
    print("Неверный пароль")
    user = input("Введите пароль:")
else:
    print("Вход выполнен")
