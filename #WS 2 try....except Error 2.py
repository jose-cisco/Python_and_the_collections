# W2 try....except Error 2

a = 5
b = eval(input('enter number: '))

try:
    c = a/b
    print(c)

except Exception as e: # except BaseException as e: เขียนแบบนี้ก็ได้
    print('Error ja --> divided by zero') 
    print(e)
