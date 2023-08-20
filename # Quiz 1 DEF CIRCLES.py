# Quiz 1 DEF CIRCLES 


r = eval(input('Enter your radiant:'))
def circles(r):
    area = 3.14*(r*r)
    perimeter = 2*3.14*r
    print('radiant={},area={},perimeter={}'.format(r,area,perimeter))
    return area,perimeter

#Main Program
a1,p1 = circles(r)
a2,p2 = circles(r)
Total_area = a1+a2
Total_perimeter = p1+p2
print('Total_area={},Total_perimeter={}'.format(Total_area,Total_perimeter))
