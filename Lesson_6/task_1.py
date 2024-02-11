# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def converter(x):
    binary = []
    string_binary = ""
    while x // 2:
        binary.append(x % 2)
        x //= 2
    binary.append(1)
    binary.reverse()
    for el in binary:
        string_binary += str(el)
    return string_binary


a = converter(int(num := input("Введите целое число: ")))
print(f"Число {num} в десятичной системе = числу {a} в двоичной системе.")
