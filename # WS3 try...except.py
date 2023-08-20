# WS3 try...except

a = 10
# b = 10
lst = [1,2,3,0,5]
c = None
for b in lst:
    try:
        c = a/b
        print('a={} b={}'.format(a,b))
        print(c)
    except Exception as e:
        print('Error ja')
        print(e)

print('end of program')
       
