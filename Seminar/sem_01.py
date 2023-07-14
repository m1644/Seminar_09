


''' Задание №1
Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток. 
'''

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
    return guessing_game

secret = int(input("Загадайте число от 1 до 100: "))
attempts = int(input("Укажите количество попыток от 1 до 10: "))

game = create_guessing_game(secret, attempts)
game()
