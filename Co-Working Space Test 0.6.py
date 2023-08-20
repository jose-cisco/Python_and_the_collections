# importing only those functions 
# which are needed 
from tkinter import *
from tkinter.ttk import *
import csv

# creating tkinter window 


def Second():
    
    def Booking():
        def SUMMIT():
            filepath='fileID.csv'

            with open(filepath,"r",encoding='utf-8')as infile:
                rd=csv.reader(infile)
                mylist=list(rd)
                print('Check FileID :',mylist)
            R=ROOM.get()
            D=DAY.get()
            M=MONTH.get()
            Y=YEAR.get()
            S=START.get()
            E=END.get()
            for lst in mylist:
                print(lst)
                if USER in lst and PASS in lst:
                    print('---Correct---')
                    print("CHECKING BOOKING:",R,D,M,Y,S,'to',E)
                    lst.append(R)
                    lst.append(D)
                    lst.append(M)
                    lst.append(Y)
                    lst.append(S)
                    lst.append(E)
                    print(lst)
                    lst1=[]
                    lst1.append(lst)
                    print(lst1)
                    fileB='fileBooking.csv'
                    with open(fileB,"a",encoding='utf-8')as outfile:
                        writer=csv.writer(outfile,lineterminator='\n')
                        writer.writerows(lst1)

                    break
                else:
                    print('---Nope---')
                    
            
            
            
            
        MONTHS_LIST =  ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        ROOM_LIST  =  ['R01','R02','B01','B02']
        TIME_LIST  =  ['09.00','10.00','11.00','12.00','13.00','14.00','15.00','16.00','17.00','18.00']
        TIME_LIST2  =  ['10.00','11.00','12.00','13.00','14.00','15.00','16.00','17.00','18.00']
        
        BOOKING=Toplevel(mywin)
        BOOKING.title('BOOKING')
        print("BOOKING")

        global ROOM
        global DAY
        global MONTH
        global YEAR

        lb=Label(BOOKING,text='ROOM')               
        lb.grid(row=0,column=0)
        ROOM=Combobox(BOOKING,values=ROOM_LIST,state="readonly")
        ROOM.current(0)
        ROOM.grid(row=1,column=0)
        
        lb=Label(BOOKING,text='DAYS')               
        lb.grid(row=0,column=1)        
        DAY=Combobox(BOOKING,values=list(range(1, 32)),state="readonly")
        DAY.current(0)
        DAY.grid(row=1,column=1)

        lb=Label(BOOKING,text='MONTHS')               
        lb.grid(row=0,column=2)        
        MONTH=Combobox(BOOKING,values=MONTHS_LIST,state="readonly")
        MONTH.current(0)
        MONTH.grid(row=1,column=2)
        
        lb=Label(BOOKING,text='YEARS')               
        lb.grid(row=0,column=3)        
        YEAR=Combobox(BOOKING,value=list(range(2019,2023)),state="readonly")
        YEAR.current(0)
        YEAR.grid(row=1,column=3)

        lb=Label(BOOKING,text='START')               
        lb.grid(row=0,column=4)        
        START=Combobox(BOOKING,value=TIME_LIST,state="readonly")
        START.current(0)
        START.grid(row=1,column=4)

        lb=Label(BOOKING,text='END')               
        lb.grid(row=0,column=5)        
        END=Combobox(BOOKING,value=TIME_LIST2,state="readonly")
        END.current(0)
        END.grid(row=1,column=5)        

        btn=Button(BOOKING,text="SUMMIT",command=SUMMIT)
        btn.grid(row=2,column=0)

        btn = Button(BOOKING,text ="Back",command=BOOKING.destroy) 
        btn.grid(row=2,column=1)
            
    def Checking():
        
        CHECKING=Toplevel(mywin)
        CHECKING.title('HISTORY')
        print("HISTORY")
        fileH='fileBooking.csv'

        with open(fileH,"r",encoding='utf-8')as infile:
            rd=csv.reader(infile)
            mylist=list(rd)
        print(mylist)
        i=0
        for lst in mylist:
            print(lst)
            if USER == lst[0]:
                i+=1
                print(i)
                P=(lst[4],lst[5],lst[6],lst[7],lst[8],'-',lst[9])
                C=Label(CHECKING,text=P)
                C.grid(row=+i,column=1,)
                print('---THIS ONE---')
            else:
                print('---Not This---')
        
        C=Label(CHECKING,text='Checking')
        C.grid(row=0,column=1,)
        
        btnB = Button(CHECKING, text ="Back",command=CHECKING.destroy) 
        btnB.grid(row=3,column=2,)
        
    print('USER :',USER)
    
    print('PASS :',PASS)
    
    print('Second')
    mywin=Tk()
    mywin.title('Co-Working Space')

    lbS=Label(mywin,text='ยินดีต้อนรับสู่ระบบการจอง')
    lbS.grid(row=1,column=2,)

    lbS2=Label(mywin,text='Co-Working Space')
    lbS2.grid(row=2,column=2,)

    btnS = Button(mywin, text ="Booking",command=Booking) 
    btnS.grid(row=3,column=2,ipadx=200)

    btnS2 = Button(mywin, text ="Checking",command=Checking) 
    btnS2.grid(row=4,column=2,ipadx=200)

    btnS3 = Button(mywin, text ="Close",command=mywin.destroy) 
    btnS3.grid(row=5,column=2,ipadx=200)

def Login():
    
    def Check():
        
        for lst in mylist:
            global USER
            global PASS
            
            USER=str(myUSER.get())
            PASS=str(myPASS.get())
            
            print('Check ID : ',USER)
            print('Check PASS: ',PASS)       
            print('Check lst :',lst)
            
            D=lst[0]
            P=lst[3]
            
            checkID=[]

            if USER == D and PASS == P:
                print('----CORRECT----')
                Second()
                Login.destroy()
                mywin.destroy()
                break
                
            else:
                print('----NOPE----')

            try:
                  print(checkID[0])
            except IndexError:
                  lb=Label(Login,text='Some ID or PASSS wrong ')               
                  lb.grid(row=0,column=1)



        
    try:
        filepath='fileID.csv'

        with open(filepath,"r",encoding='utf-8')as infile:
            rd=csv.reader(infile)
            mylist=list(rd)
    except :
        print('WTF')

    global myUSER
    global myPASS
    

    myUSER=StringVar()
    myPASS=StringVar()

    Login=Toplevel(mywin)
    Login.title('Login')
    Login.minsize(300,150)

    lb=Label(Login,text='LOGIN:')               
    lb.grid(row=0,column=0,ipadx=50)

    lb=Label(Login,text='ID/USER:')               #ID
    lb.grid(row=1,column=0)
    USER=Entry(Login,textvariable=myUSER)
    USER.grid(row=1,column=1)

    lb=Label(Login,text='Password:')            #PASS
    lb.grid(row=2,column=0)
    PASS=Entry(Login,textvariable=myPASS)
    PASS.grid(row=2,column=1)

    btok=Button(Login,text='Login',command=Check)
    btok.grid(row=3,column=0)

    btok=Button(Login,text='Back',command=Login.destroy)
    btok.grid(row=3,column=1)
        

    
def Register():
    
      def Save():
          import csv
          
          lst=[]
          lst1=[]
          
          NAME=str(myNAME.get())
          ID=str(myID.get())
          EMAIL=str(myEMAIL.get())
          PASS=str(myPASS.get())
          print('Save')
      
          lst.append(ID)
          lst.append(NAME)
          lst.append(EMAIL)
          lst.append(PASS)
          print('all save to lst')
          print(lst)
      
          lst1.append(lst)
          print('[lst] to lst1')
          print(lst1)
      
          fileID='fileID.csv'

          with open(fileID,"a",encoding='utf-8')as outfile:
              writer=csv.writer(outfile,lineterminator='\n')
              writer.writerows(lst1)
          print('lst1 has added')          
          Register.destroy()
    
            
      Register=Toplevel(mywin)
      Register.title('Register')
      Register.minsize(300,150)

      global NAME
      global myNAME
      global ID
      global myID
      global PASS
      global myPASS
      global EMAIL
      global myEMAIl

      myNAME=StringVar()
      myID=StringVar()
      myEMAIL=StringVar()
      myPASS=StringVar()

      lb=Label(Register,text='Name')               #Name
      lb.grid(row=1,column=2,ipadx=50)
      NAME=Entry(Register,textvariable=myNAME)
      NAME.grid(row=1,column=3)

      lb=Label(Register,text='ID CARD')            #ID
      lb.grid(row=2,column=2,ipadx=50)
      ID=Entry(Register,textvariable=myID)
      ID.grid(row=2,column=3)

      lb=Label(Register,text='EMAIL')              #EMAIL
      lb.grid(row=3,column=2,ipadx=50)
      EMAIL=Entry(Register,textvariable=myEMAIL)
      EMAIL.grid(row=3,column=3)

      lb=Label(Register,text='PASSWORD')           #PASSWORD
      lb.grid(row=4,column=2,ipadx=50)
      PASS=Entry(Register,textvariable=myPASS)
      PASS.grid(row=4,column=3)

      btok=Button(Register,text='SUMMIT',command=Save) #use def Save
      btok.grid(row=11,column=2)

      bt=Button(Register,text='BACK',command=Register.destroy) #Close
      bt.grid(row=12,column=2)


global mywin
mywin = Tk() 
mywin.minsize(300,150)

print('First')
mywin.title('Co-Working Space')
        
lbF=Label(mywin,text='ยินดีต้อนรับสู่ระบบการจอง')
lbF.grid(row=1,column=2,)

lbF2=Label(mywin,text='Co-Working Space')
lbF2.grid(row=2,column=2,)

btnF = Button(mywin, text ="Login",command=Login) 
btnF.grid(row=3,column=2,ipadx=200)

btnF2 = Button(mywin, text ="Register",command=Register) 
btnF2.grid(row=4,column=2,ipadx=200)
    
mainloop()
# infinite loop 
 
