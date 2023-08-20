# WS15 csv01
import csv
filepath = 'myfilecsv.csv'


with open (filepath,'r',encoding='utf-8')as infile:
    rd = csv.reader(infile)
    mylist = list(rd)  #อ่านข้อมูลทั้งหมดมาเก็บที่ตัวแปร mylist

print(mylist)
print('end of file')
