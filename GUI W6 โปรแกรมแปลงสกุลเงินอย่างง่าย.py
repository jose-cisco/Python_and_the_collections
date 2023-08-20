# GUI W6 โปรแกรมแปลงสกุลเงินอย่างง่าย 
from tkinter import *
exchange_rate = 31.5

def convert(): #ฟังก์ชันคำนวณเปลี่ยนสกุลเงิน
    input_usd = eval(my_input.get())
    thb = input_usd*exchange_rate #อ่านข้อมูลอินพุตที่ผู้ใช้กรอกข้อมูลเข้ามา
    display.set('{0:.2f} THB'.format(thb)) #แสดงผลในรูปแบบทศนิยม 2 ตำแหน่ง

mywin =Tk()

display = StringVar()
my_input = StringVar()

mywin.title('Currently Converter')
mywin.minsize(340,160)

Label(mywin,text='Please Enter USD..').pack()
inp = Entry(mywin,textvariable=my_input)
inp.pack()
inp.focus() #เพิ่มความสะดวกในการใช้งานถ้าไม่มีตัวนี้จtรันไม่ได้เลย ให้ cursor กะพริบรอในช่องที่เราจะกรอกช้อมูล

lbl = Label(mywin,textvariable=display) #Label แสดงค่าเงินที่เปลี่ยนสกุลแล้ว
lbl.pack()

btOK = Button(mywin,text='OK',width = 10 ,command=convert) #สั่งรันฟังก์ชัน convert
btOK.pack()     

bt = Button(mywin,text='Close',command=mywin.destroy,width=10)
bt.pack()

mainloop()
