# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в тексте введенном с клавиатуры

string = input("Введите любой текст: ")
characters_dict = {i: string.count(i) for i in string}
print(characters_dict)
