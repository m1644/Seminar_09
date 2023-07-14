import json
import functools
import random


def save_to_json(filename):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                'args': {
                    'secret_number': args[0],
                    'max_attempts': args[1]
                },
                'kwargs': [],
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

def validate_input(func):
    @functools.wraps(func)
    def wrapper():
        secret = int(input("Загадайте число от 1 до 100: "))
        attempts = int(input("Укажите количество попыток от 1 до 10: "))
        if not (1 <= secret <= 100) or not (1 <= attempts <= 10):
            print("Введены некорректные значения. Генерируются случайные числа.")
            secret = random.randint(1, 100)
            attempts = random.randint(1, 10)
        func(secret, attempts)
    return wrapper

def run_multiple_times(num_runs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(num_runs):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@run_multiple_times(num_runs=1)
@validate_input
@save_to_json('Seminar_dz/Game/game_data.json')
def create_guessing_game(secret_number, max_attempts):
    def guessing_game():
        attempts = 0
        while attempts < max_attempts:
            guess = int(input("Угадайте число: "))
            attempts += 1
            if guess == secret_number:
                print("Поздравляю, вы угадали число!")
                return True
            if guess < secret_number:
                print("Загаданное число больше.")
            else:
                print("Загаданное число меньше.")
        print("У вас закончились попытки. Загаданное число было:", secret_number)
        return False
    return guessing_game()
