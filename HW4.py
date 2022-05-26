# 1. Пустая функция.
def empty():
    pass


# 2. Функция фозвращает удвоенное число.
def double(num):
    return num * 2


# 3. Четное, нечетное.
def even_odd(num):
    print("yes") if num % 2 == 0 else print("no")


# 4. Первое число больше 10 или нет.
def more_10(num1, num2=2):
    if num1 > 10:
        print("да")
    elif num1 < 10:
        print("Нет")


# 5. Лямбда делит по модулю два аргумента.
h = lambda x, y: x % y


# 6. Создать функцию с декоратором
def salad(dressing):
    def ingredient():
        print("tomato")
        print("cucumber")
        dressing()

    return ingredient


@salad
def dress():
    input("What would you like to dress your salad with?")


# 7. Map and filter
animal = ["cat", "dog", "pig", "mouse"]
results = list(map(str.upper, animal))
print(results)
results = list(filter(lambda a: len(a) == 3, animal))
print(results)

# 8. чистая и нечистая функция
my_list = [32, 3, 50, 2, 29, 43]


def clean(li):
    return sorted(li)


def unclean(li):
    li.sort()
    return li


# 8. минимум и максимум
def min_max(li):
    print("Мини " + str(min(li)) + " , Макси " + str(max(li)))
min_max(my_list)



