from typing import Any, Callable
import datetime


# 1. Пустая функция.
def empty():
    pass


# 2. Функция фозвращает удвоенное число.
def double(num: int) -> int:
    return num * 2


# 3. Четное, нечетное.
def even_odd(num: int):
    print("yes") if num % 2 == 0 else print("no")


# 4. Первое число больше 10 или нет.
def more_10(num1: int, num2: int = 2):
    if num1 > 10:
        print("да")
    elif num1 < 10:
        print("Нет")


# 5. Лямбда делит по модулю два аргумента.
h: Callable[[int, int], int] = lambda x, y: x % y


# 6. Создать функцию с декоратором
def salad(dressing):
    def ingredient():
        print("tomato")
        print("cucumber")
        dressing()

    return ingredient()


@salad
def dress() -> str:
    return input("What would you like to dress your salad with?")


# 7. Map and filter
animal = ["cat", "dog", "pig", "mouse"]
results = list(map(str.upper, animal))
print(results)
results = list(filter(lambda a: len(a) == 3, animal))
print(results)

# 8. чистая и нечистая функция
my_list = [32, 3, 50, 2, 29, 43]


def clean(li: list) -> list:
    return sorted(li)


def unclean(li: list) -> list:
    li.sort()
    return li


# 8. минимум и максимум
def min_max(li: list):
    print("Мини " + str(min(li)) + " , Макси " + str(max(li)))


min_max(my_list)


# 9.  високосный год или нет.
def year() -> bool:
    x = int(input("Введите год"))
    if x % 400 == 0 or x % 4 == 0 and x % 100 != 0:
        return True
    else:
        return False


# 10. Время года
def season(month: int):
    if 13 > month > 0:
        if month < 3 or month > 11:
            print("Зима")
        elif month < 7:
            print("Весна")
        elif month < 10:
            print("Лето")
        else:
            print("Весна")
    else:
        month = (int(input("Введите месяц, число от 1 - 12")))
        season(month)


# 11. Проверка даты на существование


def date(d: int, m: int, y: int) -> bool:
    try:
        datetime.date(y, m, d)
    except ValueError:
        return False
    else:
        return True


# 12. Новый список согласно условиям.
list_1 = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']


def list_corrected(li: list) -> list:
    new_list = []
    for i in li:
        if type(i) == float or type(i) == int:
            new_list.append(i)
    return sorted(new_list)


print(list_corrected(list_1))
