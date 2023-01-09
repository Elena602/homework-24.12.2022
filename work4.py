# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

min_koef = 0     # нижняя граница для генерации коэффициентов
max_koef = 100  # верхняя граница для генерации коэффициентов

def write_file(str):
    f = open("polinom.txt", 'w')
    str = str.replace('1*x', 'x', k)
    f.write(str)
    f.close()

def create_list(k):
    list_pol = []
    list_pol.append(randint(1, max_koef))
    for i in range(1, k + 1):
        list_pol.append(randint(min_koef, max_koef))
    return list_pol

def create_str(list_koef):
    list_pol = list_koef
    str_pol = '' # строка, в которую записываем наш многочлен
    if len(list_pol) == 1: # если степень k многочлена равна 0
        str_pol = 'x = 0'
    else:
        if  list_pol[0] != 0:
            str_pol += f'{list_pol[0]}*x^{len(list_pol) - 1}'        # первый одночлен высшей степени

        for i in range(1, len(list_pol)):
            if(randint(0, 1)):                                      # выбор: добавлять ли в строку текущий отдночлен(1 - да)

                if i != len(list_pol) - 1 and list_pol[i] != 0 and i != len(list_pol) - 2: #не предпоследний одночлен, то есть степень у 'X' не ниже 2 и не равен 0
                    str_pol += ' + '                                # добавление знака перед одночленом
                    str_pol += f'{list_pol[i]}*x^{len(list_pol) - i - 1}'
                elif i == len(list_pol) - 2 and list_pol[i] != 0:   # предпоследний одночлен, не равный 0
                    if list_pol[i-1]!= 0 :
                        str_pol += ' + '                            # добавление знака перед одночленом
                    str_pol += f'{list_pol[i]}*x'
                elif i == len(list_pol) - 1 and list_pol[i] != 0:   # последний одночлен, не равный 0
                    str_pol += ' + '                                # добавление знака перед одночленом
                    str_pol += f'{list_pol[i]}'

            if i == len(list_pol) - 1 :                             # вывод в конце многочлена "= 0"
                str_pol += ' = 0'

    return str_pol

print('Введите натуральную степень k:')
k = int(input())
list_koef = create_list(k)
write_file(create_str(list_koef))