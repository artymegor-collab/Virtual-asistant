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