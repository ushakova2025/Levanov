import turtle
turtle.color("red")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.forward(400)
    turtle.right(144)
turtle.end_fill()
turtle.up()
turtle.goto(160,-75)
turtle.write("C 9 МАЯ",move=True, font=("Arial", 15, "bold"))
