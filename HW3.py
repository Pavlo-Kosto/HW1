import turtle

for i in range(4):
    turtle.forward(50)
    turtle.left(90)

turtle.penup()
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.pendown()

for i in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.exitonclick()
