import random


''' Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
'''

def validate_input(func):
    def wrapper():
        secret = int(input("Загадайте число от 1 до 100: "))
        attempts = int(input("Укажите количество попыток от 1 до 10: "))
        if not (1 <= secret <= 100) or not (1 <= attempts <= 10):
            print("Введены некорректные значения. Генерируются случайные числа.")
            secret = random.randint(1, 100)
            attempts = random.randint(1, 10)
        func(secret, attempts)
    return wrapper

@validate_input
def create_guessing_game(secret_number, max_attempts):
    def guessing_game():
        attempts = 0
        while attempts < max_attempts:
            guess = int(input("Угадайте число: "))
            attempts += 1
            if guess == secret_number:
                print("Поздравляю, вы угадали число!")
                return
            if guess < secret_number:
                print("Загаданное число больше.")
            else:
                print("Загаданное число меньше.")
        print("У вас закончились попытки. Загаданное число было:", secret_number)
    guessing_game()

create_guessing_game()
