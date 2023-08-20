# WS16 readcsv02 : sum and avg
import csv
filepath = 'myfilecsv.csv'


with open (filepath,'r',encoding='utf-8')as infile:
    rd = csv.reader(infile)
    mylist = list(rd)  #อ่านข้อมูลทั้งหมดมาเก็บที่ตัวแปร mylist

print(mylist)

sum = 0
for row in mylist:    #วนรอบตามจำนวน Row
    sum += eval(row[2]) #row[2] คือข้อมูลลำดับที่ 3 ของแต่ละบรรทัด(แต่ละ Row)ซึ่งด็คือตัวเลขที่อยู่หลังชื่อคน

avg = sum/len(mylist)
print('sum ={} avg ={}'.format(sum,avg))
print('end of file')
