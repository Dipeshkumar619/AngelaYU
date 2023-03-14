# What
# has -- Attribute -- basically variables
# does -- method -- functions
# oop is basically a blue print to generate multiple instannces of same thing.
# the module wont' be activatated unless its method/attributes are not being used.
# object.attribute  -- car.speed
# function tied to an object called as methods
# import some_module
# import turtle as t
# print(some_module.module_variable)
# myscreen=t.Screen()
# myscreen.bgcolor("black")
# print(myscreen.canvwidth,myscreen.canvwidth)
# timmy=t.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('green')
# position=timmy.position()
# print(position)
# forward=0
# angle=0
# distance=20
# while True:
#     timmy.forward(distance)
#     timmy.left(angle)
#     angle=+10
#     distance=+10
#     allpos=timmy.position
#
# myscreen.exitoncli
from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Global PokeMons",["Pikachu","Squirtle","keras"],"l")
table.add_column("PokeMons Type",["electric","Water","Fire"])
print(table)