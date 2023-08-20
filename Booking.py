#Booking
from tkinter  import *
from tkinter  import ttk  # ttk -> themed tk (for Combobox)
from datetime import date
from time     import strftime

def booking(e):
    print(cbo_day.get(),cbo_month.get(),cbo_year.get(),cbo_start_time.get(),cbo_end_time.get())
    mm = month_list.index(cbo_month.get()) + 1
    bd = date(int(cbo_year.get()), mm, int(cbo_day.get()))
    tm = time_list.index(cbo_time.get()) + 1
    print(bd,tm)

time_list = ['09.00','10.00','11.00','12.00',
        '13.00','14.00','15.00','16.00','17.00','18.00']
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
              'Dec']
root = Tk()
root.option_add("*Font", "consolas 25")
cbo_day = ttk.Combobox(root, values=list(range(1, 32)), width=3, state="readonly")
cbo_day.current(0)
cbo_day.pack(side=LEFT)

cbo_month = ttk.Combobox(root, values=month_list, width=4, state="readonly")
cbo_month.current(0)
cbo_month.pack(side=LEFT)

cbo_year = ttk.Combobox(root, values=list(range(2019, 2040)), width=5)
cbo_year.current(0)
cbo_year.pack(side=LEFT) 

cbo_time = ttk.Combobox(root,values=time_list,width = 6 ,state = "readonly")
cbo_time.current(0)
cbo_time.pack(side=LEFT)

cbo_time = ttk.Combobox(root,values=time_list,width = 6 ,state = "readonly")
cbo_time.current(1)
cbo_time.pack(side=LEFT)

btn = Button(root, text="Submit")
btn.pack()
btn.bind("<Button-1>",booking)



btHm = Button(root,text='Home',command=root.destroy).pack()
bt = Button(root,text='Close',command=root.destroy).pack()



root.mainloop()
