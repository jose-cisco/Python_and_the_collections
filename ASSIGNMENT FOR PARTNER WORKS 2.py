# ASSIGNMENT FOR PARTNER WORKS 2
print('BOOKED CO-WORKING SPACE ROOM')
lst1 = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
lst6 = []
NAME       = str(input('Enter your NAME here: '))
ID_CARD    = str(input('Enter your ID_CARD here: '))
PASSWORD   = int(input('Enter your PASSWORD here: '))
EMAIL      = str(input('Enter your EMAIL here: '))
TIMES      = str(input('Enter your TIMES here: '))
HOURS      = eval(TIMES)

lst1.append(NAME)
lst2.append(ID_CARD)
lst3.append(PASSWORD)
lst4.append(EMAIL)
lst5.append(TIMES)
lst6.append(HOURS)




lst1.extend(lst2),lst3.extend(lst4),lst5.extend(lst6)
print('{}''{}''{}'.format(lst1,lst3,lst5))
print('Number of NAMES equals{},Number of ID_CARD equals{}'.format(len(lst1),len(lst2)))
print('Number of PASSWORD equals{},Number of EMAIL equals {}'.format(len(lst3),len(lst4)))
print('Number of TIMES equals{},The Amount of HOURS are {}'.format(len(lst5),len(lst6)))
