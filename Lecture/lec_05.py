from typing import Callable


######## Замыкание

#### Множественное декорирование

def deco_a(func: Callable):
    def wrapper_a(*args, **kwargs):
        print('Старт декоратора А')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Завершение декоратора А')
        return result
    print('Возвращение декоратора А')
    return wrapper_a

def deco_b(func: Callable):
    def wrapper_b(*args, **kwargs):
        print('Старт декоратора B')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Завершение декоратора B')
        return result
    print('Возвращение декоратора B')
    return wrapper_b

def deco_c(func: Callable):
    def wrapper_c(*args, **kwargs):
        print('Старт декоратора C')
        print(f'Запускаю {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Завершение декоратора C')
        return result
    print('Возвращение декоратора C')
    return wrapper_c

@deco_c
@deco_b
@deco_a
def main():
    print('Старт основной функции')

if __name__ == '__main__':
    print('>>> Запуск main()')
    main()
    print('>>> Завершение main()')
print('------------------------')
