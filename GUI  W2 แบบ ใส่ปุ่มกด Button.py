# GUI W2
from tkinter import *

mywin = Tk()
mywin.title('Com programming 1') # ข้อความบนแท็บซ้ายสุดของกรอบหน้าต่าง
mywin.minsize(220,80) # minsize = ขนาดหน้าต่าง
lb = Label(mywin,text='Hello ja Com pro สวัสดี')
lb.pack()

bt = Button(mywin,text='Close',command=mywin.destroy) # Button = ปุ่มกด
bt.pack()

mywin.mainloop()
