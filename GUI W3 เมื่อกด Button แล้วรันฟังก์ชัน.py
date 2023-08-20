# GUI W3
from tkinter import *
def sayhello(): # สร้างฟังก์ชัน sayhello()
    print('Hello test สวัสดี') # ทดสอบแสดงข้อมูล
    lb.config(text='ปุ่มถูกกด...สวัสดีจ้า ksb')
    # lb['text'] = 'text' เขียนแบบนี้ก็ได้ คือจะเขียน lb.config หรือ lb[text] = 'text' ก็ได้
                          

mywin = Tk()
mywin.title('Com programming 1') # ข้อความบนแท็บซ้ายสุดของกรอบหน้าต่าง
mywin.minsize(200,80) # minsize = ขนาดหน้าต่าง
lb = Label(mywin,text='Hello ja Com pro สวัสดี')
lb.pack()

btOK = Button(mywin,text='OK',command=sayhello) # ButtonOK = ปุ่มกด OK , command คือการใช้ฟังค์ชันที่เราสร้าง
btOK.pack() #sayhello() เท่ากับว่าเป็น Callback หรือ Event Handler
bt = Button(mywin,text='Close',command=mywin.destroy) # Button = ปุ่มกด
bt.pack()

mywin.mainloop()
