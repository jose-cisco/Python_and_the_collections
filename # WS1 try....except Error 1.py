# try....except Error 1

a = 5
b = eval(input('enter number: '))

try:
    c = a/b
    print(c)

except ZeroDivisionError as e:
    print ('Error ja --> divided by zero')
    print(e)
