from typing import Callable


######## Замыкание

#### Области видимости и функции первого класса

def func(a):
    x = 1
    res = x + a
    return res

x = 100
print(func(5))
print('------------------------')


def add_str(a: str, b: str) -> str:
    return a + ' ' + b

print(add_str('Hello', 'world'))
print('------------------------')


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str

print(add_one_str('Hello')('world!'))
print('------------------------')
