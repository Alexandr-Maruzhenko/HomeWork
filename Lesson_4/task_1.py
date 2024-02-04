# Заполнить список степенями числа 2 (от 2^1 до 2^n)

maximum_degree = int(input("Введите максимальную степень числа: "))
list_of_numbers = [pow(2, i+1) for i in range(maximum_degree)]
print(list_of_numbers)
