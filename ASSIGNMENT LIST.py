#ASSIGNMENT LIST CALCULATING PRODUCT USING PRICE 
mylist=[]

loop = True
while loop:
    price = int(input('Enter product price(0=exit): '))
    mylist.append(price)
    amount = sum(mylist)
    if price <=0:
        loop = False

print('Total net = {:2} THB'.format(amount))

    
