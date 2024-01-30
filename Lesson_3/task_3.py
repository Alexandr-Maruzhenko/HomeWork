# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
#
# ЗАПРОС ДАННЫХ -----------------------------------------
name = input("Введите ваше имя: ")
age = input("Введите Ваш возраст: ")
city = input("Введите Ваш город: ")
#
# ФОРМИРОВАНИЕ РЕЗУЛЬТАТА СПОСОБ 1 ----------------------
data = {"user_name": name, "user_age": age, "user_city": city}
message_1 = "Приветствую тебя %(user_name)s! Я рад, что твой возраст %(user_age)s и ты из города %(user_city)s!" % data
#
# ФОРМИРОВАНИЕ РЕЗУЛЬТАТА СПОСОБ 2 ----------------------
message_2 = ("Приветствую тебя {user_name}! Я рад, что твой возраст {user_age} и ты из города {user_city}!"
             .format(user_name=name, user_age=age, user_city=city))
#
# ФОРМИРОВАНИЕ РЕЗУЛЬТАТА СПОСОБ 3 ----------------------
message_3 = f"Приветствую тебя {name}! Я рад, что твой возраст {age} и ты из города {city}!"
#
# ВЫВОД РЕЗУЛЬТАТОВ -------------------------------------
print(message_1)
print(message_2)
print(message_3)
