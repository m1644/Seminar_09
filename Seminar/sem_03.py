import json
import functools


''' Задание №3
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. 
При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
'''

def save_to_json(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                'args': args,
                'kwargs': kwargs,
                'result': result
            }
            try:
                with open(filename, 'r') as file:
                    try:
                        saved_data = json.load(file)
                        saved_data.append(data)
                    except json.JSONDecodeError:
                        saved_data = [data]
            except FileNotFoundError:
                saved_data = [data]
            with open(filename, 'w') as file:
                json.dump(saved_data, file, indent=4)
            return result
        return wrapper
    return decorator

@save_to_json('Seminar/function_plus.json')
def function_plus(a, b, c):
    return a + b + c

@save_to_json('Seminar/greet.json')
def greet(name):
    return f"Hello, {name}!"

function_plus(2, 3, 4)
function_plus(10, 20, 30)
greet('Max')
greet('John')
