import turtle as tt
leg = 120

tt.pendown()
tt.pensize(4)
tt.pencolor("blue")

tt.setheading(0)
tt.forward(leg)

for i in range(3):
    tt.left(90)
    tt.forward(leg)
