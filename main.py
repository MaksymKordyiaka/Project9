'''
1. Створити функцію, яка в якості аргументів прийматиме рандомну кількість парних
елементів (словник), після чого ці пари мають бути записані в окремий текстовий
файл, в форматі- «key = value»

2. Створити функцію- генератор, яка може з файлу (завдання №1) прочитати всі
елементи, перетворити їх на словник та по одному повертатиме пари ключ/значення
у форматі кортежу.
'''
text = open('text.txt', 'w', encoding='utf-8')
def func1(**kwargs):
    for i, j in kwargs.items():
        text.write(f'{i}: {j}\n')
    return kwargs
n = func1(name = 'Максим', age = 19, course = 'python developer')

def func2(*args):
    for i in n.items():
        text.write(f'{i}\n')
    yield args
m = func2(text)
next(m)