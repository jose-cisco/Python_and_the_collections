# GUI BOOKING ROOM
from tkinter import *
def sayhello(): # สร้างฟังก์ชัน sayhello()
    print('TEST1') # ทดสอบแสดงข้อมูล
    lb.config(text='Booking CWSR')
    # lb['text'] = 'text' เขียนแบบนี้ก็ได้ คือจะเขียน lb.config หรือ lb[text] = 'text' ก็ได้
                          

mywin = Tk()
mywin.title('Com programming 1') # ข้อความบนแท็บซ้ายสุดของกรอบหน้าต่าง
mywin.minsize(400,200) # minsize = ขนาดหน้าต่าง
lb = Label(mywin,text=' ')
lb.pack()

btA01 = Button(mywin,text='A01',command=sayhello,width=10).pack() # ButtonOK = ปุ่มกด OK , command คือการใช้ฟังค์ชันที่เราสร้าง
#btbK.pack() #sayhello() เท่ากับว่าเป็น Callback หรือ Event Handler
btA02 = Button(mywin,text='A02',command=sayhello,width=10).pack() # Button = ปุ่มกด
btB01 = Button(mywin,text='B01',command=sayhello,width=10).pack()
btB02 = Button(mywin,text='B02',command=sayhello,width=10).pack()
bt    = Button(mywin,text='Close',command=mywin.destroy,width=10).pack()
mywin.mainloop()
