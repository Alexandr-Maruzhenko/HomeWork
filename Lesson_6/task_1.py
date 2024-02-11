# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def converter_bin(x):
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


def converter_dec(x):
    number_dec = 0
    binary_list = list(map(int, list(x)))
    binary_list.reverse()
    for id, val in enumerate(binary_list):
        number_dec += val * pow(2, id)
    return number_dec


numb_bin = converter_bin(int(num := input("Введите целое число: ")))
print(f"Число {num} в десятичной системе = числу {numb_bin} в двоичной системе.")
numb_dec = converter_dec(numb_bin)
print(f"Число {numb_bin} в двоичной системе = числу {numb_dec} в десятичной системе.")
