# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = float(input("Введите число для заданной точности числа Пи:\n"))
i = 0
while d < 1:
    d = d * 10
    i += 1
if i > 10: print(f'Не соответствует установленным значениям d') 
print(f'число Пи с заданной точностью равно {round(pi, i)}')
