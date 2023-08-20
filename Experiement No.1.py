

import turtle as tt
Dimension = 8
Distance = 12
tt.width(8)
tt.pencolor("blue")
for a in range(3):
    if a in range(1,6,2):
        tt.pd()
        tt.fd(Dimension)
        tt.lt(90)
        tt.fd(Dimension)
        tt.rt(90)
        tt.fd(Dimension)
        tt.lt(90)
        tt.fd(Dimension)
        tt.rt(90)
        tt.pu()
for b in range(3):
        for b in range(2,7,2):
            tt.pd()
            tt.fd(Dimension)
            tt.lt(60)
            tt.fd(Dimension)
            tt.rt(60)
            tt.fd(Dimension)
            tt.lt(60)
            tt.fd(Dimension)
            tt.rt(60)
            tt.fd(Dimension)
            tt.lt(60)
            tt.fd(Dimension)
            tt.rt(60)
            tt.fd(Dimension)
            tt.pu()

tt.home()
