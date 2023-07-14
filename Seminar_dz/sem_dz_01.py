import csv
import json
import random
from functools import wraps
from math import sqrt


''' Задание_1
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
'''

def find_roots(a, b, c):
    """Нахождение корней квадратного уравнения"""
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return None

def generate_csv(filename, rows):
    """Генерация csv файла с тремя случайными числами в каждой строке"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

def roots_decorator(func):
    """Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла"""
    @wraps(func)
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Корни для {a}, {b}, {c}: {result}")
    return wrapper

def save_results_decorator(func):
    """Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            'args': args,
            'kwargs': kwargs,
            'result': result
        }
        with open('Seminar_dz/results.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        return result
    return wrapper


@roots_decorator
def find_roots_csv(a, b, c):
    return find_roots(a, b, c)

@save_results_decorator
def example_function(param1, param2):
    return param1 + param2

generate_csv('Seminar_dz/numbers.csv', random.randint(100, 1000))

find_roots_csv('Seminar_dz/numbers.csv')

example_function(5, 10)
