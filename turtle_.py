from turtle import *

pensize(4)
shape('turtle')
color('green')
coord = [-200, 200, 0]
fillcolor('yellow')
for j in range(3):
    begin_fill()
    for i in range(3):
        forward(100)
        lt(120)
    end_fill()
    penup()
    goto(coord[j], 0)
    pendown()








mainloop()