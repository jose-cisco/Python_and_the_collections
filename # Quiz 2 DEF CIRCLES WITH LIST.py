# Quiz 2 DEF CIRCLES WITH LIST

lst=[]
r1 = eval(input('Enter your radiant:'))
r2 = eval(input('Enter your radiant:'))
def circles(r):
    area = 3.14*(r*r)
    perimeter = 2*3.14*r
    print('radiant={:.2f},area={:.2f},perimeter={:.2f}'.format(r,area,perimeter))
    return area,perimeter

#Main Program
a1,p1 = circles(r1) 
a2,p2 = circles(r2)
Total_area = a1+a2
Total_perimeter = p1+p2
lst.append(Total_area)
lst.append(Total_perimeter)
lst.append(a1) #เอาค่า a1 มาใช้ได้เลย เพราะ a1 คือ area ของวงกลมแรก
lst.append(p1) #เอาค่า a2 มาใช้ได้เลย เพราะ a1 คือ area ของวงกลมสอง
lst.append(a2) #เอาค่า p1 มาใช้ได้เลย เพราะ p1 คือ perimeter ของวงกลมแรก
lst.append(p2) #เอาค่า p2 มาใช้ได้เลย เพราะ p2 คือ perimeter ของวงกลมสอง
print(lst))
