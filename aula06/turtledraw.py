# Exercise 5 on "How to think like a computer scientist", ch. 11.
from tkinter import filedialog
import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
filename = filedialog.askopenfilename(title="Choose File")

with open(filename, 'r') as doc:
    for line in doc:
        if line.endswith('\n'):
            line = line[:-1]
        if line == 'UP':
            t.up()
        elif line == 'DOWN':
            t.down()
        else:
            lst = line.split(' ')
            print(lst)
            t.goto(float(lst[0]), float(lst[1]))

# wait
turtle.Screen().exitonclick()

