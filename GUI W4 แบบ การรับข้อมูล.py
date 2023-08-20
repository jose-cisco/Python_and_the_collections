# GUI W4
from tkinter import *
def sayhello(): # สร้างฟังก์ชัน sayhello()
    the_input = my_input.get() # อ่านข้อมูลอินพุตที่ผู้ใช้กรอกมา
    print('you entered =>',the_input)
    lb['text'] = 'the_input'
    # lb['text'] = 'text' เขียนแบบนี้ก็ได้ คือจะเขียน lb.config หรือ lb[text] = 'text' ก็ได้
                          

mywin = Tk()
mywin.title('Com programming 1') # ข้อความบนแท็บซ้ายสุดของกรอบหน้าต่าง
mywin.minsize(360,140) # minsize = ขนาดหน้าต่าง\

my_input = StringVar() # ประกาศตัวแปรที่รับข้อมูลอินพุต
lb = Label(mywin,text='Hello ja Com pro สวัสดี')
lb.pack()

ent = Entry(mywin,textvariable = my_input)#Widget กรอบรับข้อมูล
ent.pack()

btOK = Button(mywin,text='OK',command=sayhello,width=10) # ButtonOK = ปุ่มกด OK , command คือการใช้ฟังค์ชันที่เราสร้าง
btOK.pack() #sayhello() เท่ากับว่าเป็น Callback หรือ Event Handler

bt = Button(mywin,text='Close',command=mywin.destroy,width=10) # Button = ปุ่มกด
bt.pack()

mywin.mainloop()
