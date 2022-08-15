import prettytable

import another_module
print(another_module.another_variable)

# import turtle
#
# timmy = turtle.Turtle()

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
#
# timmy.shape("turtle")
# timmy.shape()
# timmy.color("red")
# timmy.forward(200)
# my_screen = Screen()
#
# my_screen.exitonclick()
# print(my_screen.canvwidth)

from prettytable import PrettyTable
#
poke_table = PrettyTable()
poke_table.field_names = ["Pokemon Name", "Pokemon Type"]
poke_table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"],
    ]
)

print(poke_table)


# x = PrettyTable()
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# x.add_row(["Adelaide", 1295, 1158259, 600.5])
# print(x)


