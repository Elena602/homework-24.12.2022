# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
numbers = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {numbers}")
unique_numbers = list(set(numbers))
print(f"Список из неповторяющихся элементов: {unique_numbers}")