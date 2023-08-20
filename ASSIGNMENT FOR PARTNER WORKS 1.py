# ASSIGNMENT FOR PARTNER WORKS 1
print('WELCOME TO CO-WORKING SPACE ROOM')

lst1 = []
lst2 = []
lst3 = []
lst4 = []
NAME       = str(input('Enter your NAME here: '))
ID_CARD    = str(input('Enter your ID_CARD here: '))
PASSWORD   = int(input('Enter your PASSWORD here: '))
EMAIL      = str(input('Enter your EMAIL here: '))
lst1.append(NAME)
lst2.append(ID_CARD)
lst3.append(PASSWORD)
lst4.append(EMAIL)
lst1.extend(lst2),lst3.extend(lst4)

print('{}''{}'.format(lst1,lst3))
print('Number of NAMES equals {:4}, Number of ID_CARD equals{}'.format(len(lst1),len(lst2)))
print('Number of PASSWORD equals {},Number of EMAIL equals{:2}'.format(len(lst3),len(lst4)))
