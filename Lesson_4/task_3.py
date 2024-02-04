# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

count_users = int(input("Введите количество пользователей: "))
print("---------")
main_dictionary = {i: {'name': "", 'email': ""} for i in range(count_users)}
for i in main_dictionary:
    name = input("Имя пользователя " + str(i+1) + ": ")
    email = input("E-mail пользователя " + str(i+1) + ": ")
    main_dictionary[i]["name"] = name
    main_dictionary[i]["email"] = email
    print("---------")
print(main_dictionary)
