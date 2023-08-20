#WS1: list given total element

print('Welcome to KSB store')

mylist = []
total_element = eval(input("Enter number of products: "))

for i in range(total_element):
    data_i = eval(input("value for"+str(i)+": "))
    mylist.append(data_i)

print(mylist)
amount = sum(mylist)
print('{} product(s) in your cart. Total={} THB'.format(len(mylist),amount))
