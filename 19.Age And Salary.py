#age&salary

loop = True
while loop:
    age = int(input('Enter your age(<60=exit): '))
    if age in range(60,66):
        salary = "500บาท/เดือน"
    elif age in range(66,71):
        salary = "600บาท/เดือน"
    elif age in range(71,76):
        salary = "800บาท/เดือน"
    elif age in range(76,81):
        salary = "900บาท/เดือน"
    elif age>=81:
        salary = "1000บาท/เดือน"
    else:
        age<60
    loop = False

print('{:2} ปี ได้ {:2}'.format(age,salary))
