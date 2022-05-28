# import turtle
#
# for i in range(4):
#     turtle.forward(50)
#     turtle.left(90)
#
# turtle.penup()
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.pendown()
#
# for i in range(2):
#     turtle.forward(100)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.left(90)
# turtle.exitonclick()

# Дополняю домашку из заданий в презентации.
# Пароль
password = "dodo"
man1 = input("Введите пароль")
try_p = 1
while (man1 != password) and (try_p != 5):
    try_p += 1
    man1 = input("Введите пароль")
if man1 == password:
    print("красавчиг")
else:
    print("До встречи")


