from tkinter import *
from tkinter import ttk  # ttk -> themed tk (for Combobox)
from datetime import date


def on_click(e):
    print(cbo_day.get(), cbo_month.get(), cbo_year.get())
    mm = month_list.index(cbo_month.get()) + 1
    bd = date(int(cbo_year.get()), mm, int(cbo_day.get()))
    print(bd)
    
  def create_widgets(self):
    #add label for number
    self.label1 = Label(self)
    self.label1["text"] = "Number :" 
    self.label1.grid(column=1, row=2)
    
    # create combobox for select number
    self.box = Combobox(self)
    self.box['values'] = ('1', '2', '3', '4', '5')
    self.box.current(0)
    self.box.bind("<<>ComboboxSelected>")
    self.box.grid(column=2, row=2)

    # create print button
    self.button = Button(self)
    self.button["text"] = "Print"
    self.button["command"] = self.print_number
    self.button.grid(column=2, row=3)
    
  # copy source file from eimer to destination folder
  def print_number(self):
    print("hi there, everyone! " + self.box.get())

# for debug
if __name__=="__main__":
  root = Tk()
  root.title("Lebeller")
  root.geometry("350x200")

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

btn = Button(root, text="submit")
btn.pack()
btn.bind("<Button-1>", on_click)

root.mainloop()
