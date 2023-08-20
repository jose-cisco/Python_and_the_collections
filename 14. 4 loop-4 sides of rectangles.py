import turtle as tt

distance = 100
leg = 80

tt.pensize(4)
tt.pencolor("blue")

for a in range(3):
    for k in range(4):
        tt.pendown()
        tt.forward(leg)

        for i in range(3):
            tt.left(90)
            tt.forward(leg)

        tt.penup()
        tt.setheading(0)
        tt.forward(distance)

    tt.home()
    tt.sety(-100*(a+1))
    

            
