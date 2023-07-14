from typing import Callable


######## Замыкание

#### Замыкаем изменяемые объекты

def add_one_str(a: str) -> Callable[[str], str]:
    names = []
    
    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)
    return add_two_str

hello = add_one_str('Hallo')
bye = add_one_str('Good bye')

print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
print('------------------------')


#### Замыкаем неизменяемые объекты

def add_one_str1(a: str) -> Callable[[str], str]:
    text = ''
    
    def add_two_str1(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text
    return add_two_str1

hello = add_one_str1('Hallo')
bye = add_one_str1('Good bye')

print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))
print('------------------------')


#### Задача_1

def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}
    
    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d
    return loc

small = main(42)
big = main(73)
print(small(7), big(7), small(3))
print('------------------------')
