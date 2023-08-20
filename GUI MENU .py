# GUI MENU
from tkinter import *
def sayhello(): # สร้างฟังก์ชัน sayhello()
    print('TEST1') # ทดสอบแสดงข้อมูล
    lb.config(text='Booking CWSR')
    # lb['text'] = 'text' เขียนแบบนี้ก็ได้ คือจะเขียน lb.config หรือ lb[text] = 'text' ก็ได้
                          

mywin = Tk()
mywin.title('Com programming 1') # ข้อความบนแท็บซ้ายสุดของกรอบหน้าต่าง
mywin.minsize(400,150) # minsize = ขนาดหน้าต่าง
lb = Label(mywin,text=' ')
lb.pack()

btBK = Button(mywin,text='BOOKING',command=sayhello,width=10).pack() # ButtonOK = ปุ่มกด OK , command คือการใช้ฟังค์ชันที่เราสร้าง
#btbK.pack() #sayhello() เท่ากับว่าเป็น Callback หรือ Event Handler
btCK = Button(mywin,text='CHECKING',command=sayhello,width=10).pack() # Button = ปุ่มกด
bt = Button(mywin,text='Close',command=mywin.destroy,width=10).pack()
mywin.mainloop()
