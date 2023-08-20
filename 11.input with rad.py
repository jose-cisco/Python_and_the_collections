#input with rad

loop = True
while loop:
    rad = eval(input('Enter radius of Circle: '))
    if rad>0:
        loop = False
    print('Area of circle is...',rad*rad*3.14)

