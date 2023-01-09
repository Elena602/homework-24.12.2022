# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
from itertools import groupby


def add_poly(*args):
    sort_val = sorted([(e, v) for poly in args for v, e in poly])   # сортировка кортежей значений в одном списке
    return [
        (sum(v for _, v in g), e)                                   # cуммирование всех значений с разными степенями
        for e, g in groupby(sort_val, key=lambda kv: kv[0])         # группировка всех значений по степени от меньшей к большей
    ]


def parsing(poly): # разделеение строки на кортеж коэффициентов
    data = []
    poly = poly.split(' + ') # признак разделения
    for i in poly:
        if '*x^' in i: # проверка на степень(если 2-я и выше)
            data.append((int(i.split('*x^')[0]), int(i.split('*x^')[1])))
        elif '*x' in i: # проверка на степень(если 1-я)
            data.append((int(i[0]), 1))
        else:
            data.append((int(i), 0))
    return data


def sum_pol(added):
    solution = ''
    solution += str(added[len(added) - 1][0]) + '*x^' + str(added[len(added) - 1][1])
    for i in range(len(added) - 2, -1, -1):
        if added[i][1] == 0: # нулевая степень
            solution += ' + ' + str(added[i][0])
        if added[i][1] == 1: # первая степень
            solution += ' + ' + str(added[i][0]) + '*x'
        if added[i][1] != 1 and added[i][1] != 0: # не нулевая и не первая степень
            solution += ' + ' + str(added[i][0]) + '*x^' + str(added[i][1])
    return solution

file1 = 'poly_1.txt'
file2 = 'poly_2.txt'

def read_pol(file):  # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

p1 = read_pol(file1) # строки из файлов
# '12*x^4 + 21*x^3 + 62*x^2 + 7*x + 6'
p2 = read_pol(file2)
# '5*x^2 + 2*x + 5'
# print(comp(add_poly(parsing(p1), parsing(p2))))
print('Итоговый результат сложения полиномов:\n', sum_pol(add_poly(parsing(p1), parsing(p2))))
with open('task.txt', 'w') as file_sum:
    file_sum.writelines(sum_pol(add_poly(parsing(p1), parsing(p2))))