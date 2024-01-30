# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
#
# ОБНУЛЕНИЕ СЧЁТЧИКОВ ----------------------------------
negative_number_counter = 0
positive_number_counter = 0
zero_counter = 0
#
# ЗАПРОС ЧИСЕЛ -----------------------------------------
number_1 = int(input("Введите число №1: "))
number_2 = int(input("Введите число №2: "))
number_3 = int(input("Введите число №3: "))
#
# ПРОВЕРКИ (ПРИМИТИВНО И НЕ КРАСИВО )-------------------
if number_1 < 0:
    negative_number_counter += 1
elif number_1 == 0:
    zero_counter += 1
else:
    positive_number_counter += 1

if number_2 < 0:
    negative_number_counter += 1
elif number_2 == 0:
    zero_counter += 1
else:
    positive_number_counter += 1

if number_3 < 0:
    negative_number_counter += 1
elif number_3 == 0:
    zero_counter += 1
else:
    positive_number_counter += 1
#
# ФОРМИРОВАНИЕ И ВЫВОД РЕЗУЛЬТАТА ----------------------
message = f"Отрицательных чисел {negative_number_counter}, положительных чисел {positive_number_counter}, нулей {zero_counter}"
print(message)
