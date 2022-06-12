from typing import Any


# задача 2
def func_any(name: str, height: int, weight: int) -> Any:
    human = f"Его имя: {name}, рост {height}, вес {weight}."
    return human


print(func_any("Паша", 179, 63))


# задача 3 str -> int
def func_str_num(num: str) -> int:
    num = int(num)
    return num


print(func_str_num("22"))


# задача 4 декоратор возводящий в степень
def calc(dec):
    def sum_num():
        power = dec()
        x = int(input("В какую степень возвести?"))

        print("Степень из", x, "суммы чисел x,y =", power ** x)

    return sum_num


@calc
def step():
    print("Сложим 2 числа")
    x = int(input("ведите первое число x"))
    y = int(input("ввведите второе число y"))
    xy = x + y
    print("Сумма чисел = ", xy)
    return xy


step()

задача 5 yield next * 5
wtf = (123, 'try', 1992, 2001, 'who', 'when')


def test(x):
    for i in x:
        yield i


a = test(wtf)
x = 0
for i in range(4):
    x += 1
    next(a)
    if x == 4:
        print(next(a))
