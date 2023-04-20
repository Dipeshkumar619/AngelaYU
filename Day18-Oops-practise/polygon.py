from turtle import Turtle, Screen

oturtle = Turtle()
screen = Screen()
# screen.bgcolor("black")
oturtle.color("green")
# [180°(n) – 360°] / n
for num_sides in range(3, 20):
    interior_angle =  360 / num_sides
    print(f"the interior angle is",interior_angle)
    print(f"the number of sides are ", num_sides)
    for _ in range(num_sides):
        oturtle.forward(100)
        oturtle.right(interior_angle)
        print(f"Drawing the interior angle is", interior_angle)
        print(f"Drawing the number of sides are ", num_sides)




