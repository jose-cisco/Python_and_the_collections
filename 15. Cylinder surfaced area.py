from math import pi

while True:
    r,h = (eval(input('Enter radiant,height:')))
    if r and h >0:
        break
    print('radient and height')

Cylinder_surface_area = 2*pi*(r+h)
print('Cylinder_surface_area:{}'.format(Cylinder_surface_area))
