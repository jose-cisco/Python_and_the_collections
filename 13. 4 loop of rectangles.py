import turtle as tt

distance = 150
leg = 120

tt.pensize(4)
tt.pencolor("blue")

for k in range(4):
    tt.pendown()
    tt.forward(leg)

    for i in range(3):
        tt.left(90)
        tt.forward(leg)

    tt.penup()
    tt.setheading(0)
    tt.forward(distance)
