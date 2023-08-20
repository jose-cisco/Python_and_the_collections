# GUI W5 set method

from tkinter import *

def sayhello():
    the_input = my_input.get()
    print('you entered =>',the_input)
    display.set(the_input)

mywin = Tk()
mywin.title('Com programming 1')
mywin.minsize(360,140)

my_input = StringVar()
display = StringVar()

lb = Label(mywin,textvariable=display,text='Hello ja Com pro สวัสดี')
lb.pack()

ent = Entry(mywin,textvariable=my_input)
ent.pack()
ent.insert(END,'your name')

btOK = Button(mywin,text='OK',command=sayhello,width=10)
btOK.pack()

bt = Button(mywin,text='Close',command=mywin.destroy,width=10)
bt.pack()
mywin.mainloop()
