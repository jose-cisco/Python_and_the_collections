import turtle as tt

angle = 45
leg = 120

tt.pendown()
tt.pensize(4)
tt.pencolor("blue")
tt.setheading(angle)
tt.forward(leg)

angle += 90
tt.setheading(angle)
tt.forward(leg)

angle += 90
tt.setheading(angle)
tt.forward(leg)

angle += 90
tt.setheading(angle)
tt.forward(leg)
tt.penup()

tt.sety(-30)
tt.write("My Diamond",True,align="center" ,font=("Arial",12,"normal"))
tt.home()
