def calArea(a,b):
    area      = a*b
    perimeter = 2*(a+b)
    print('Length:{} Width:{}'.format(a,b))
    print('area=',area)
    print('perimeter=',perimeter)
    return area
# main program
rec1 = calArea(2,3)
rec2 = calArea(1,3)
rec3 = calArea(3,4)
total_area = rec1 + rec2 + rec3

print('total_area',total_area)
