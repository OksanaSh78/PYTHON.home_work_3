# Задача №11
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_number = int(input('Enter number: '))
division_list = []
division_list.insert(0, decimal_number)
for i in range(1, len(division_list)):
    if (decimal_number >= 1):
        division_list.append(decimal_number // 2)
        decimal_number = decimal_number // 2
    else:
        division_list.append(0)
 
binary_list = [len(division_list)]
for i in range(len(binary_list))[::-1]:
    if (division_list[i] % 2 == 0):
        binary_list.append(0)
    else:
        binary_list.append(1)
print(binary_list)