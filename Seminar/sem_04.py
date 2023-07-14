import functools


''' Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.
'''

def run_multiple_times(num_runs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_runs):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@run_multiple_times(num_runs=3)
def func_hello():
    print("Hello, world!")

@run_multiple_times(num_runs=2)
def func_plus(a, b):
    return print(f'{a} + {b} = {a + b}')

func_hello()
func_plus(4, 4)
