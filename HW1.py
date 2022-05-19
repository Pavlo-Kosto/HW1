name = "Pavel"
color = "Turquoise"
musical_group = "Simple plan"
movie = "The Fifth Element"
print("My name is ", name," . ", "My favorite color is ", color,", " "musical group is", musical_group,", " "movie is", movie, sep="")
# Написать список мужских и женских имен, вывести только женские имена.
names = ["Жанна", "Паша", "Марина", "Гена"]
print(names[0::2])
# Написать генератор списка, который создаст список, состоящий только из элементов с нечётным количеством цифр.
list1 = [i for i in range(0, 110) if i < 10 or i > 99]
print(list1)
list2=[j for j in [i for i in range(1,1000)] if len(str(j)) %2 != 0]
print(list2)
