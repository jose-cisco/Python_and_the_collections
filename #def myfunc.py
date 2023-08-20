#def myfunc

x = 1    # ตัวแปรนอกฟังก์ชันเรียกว่า global variables
y = 2
def myfunc():
    x = 8  #ตัวแปรในฟังก์ชันเรียกว่า local variables
    print('in function x={} y ={}'.format(x,y))
    return x

# Main program
if __name__ == '__main__':
    myfunc() #พอหลุดออกมานอกฟังก์ชัน x จะใช้ global variable แทน
    print('in Main Prg x={} y ={}'.format(x,y))
