#input using while loop

loop = True
while loop:
    val = float(input('Enter value(0=exit):'))
    if val>0:
        loop = False

    print(val)
