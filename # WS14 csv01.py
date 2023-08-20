# WS14 csv01
import csv
filepath = 'myfilecsv.CSV'

lst = [[1,'กอบเกียรติ',25],
      [2,'KSB',14],
      [3,'ณิแนน',18],
      [4,'Nancy',22]
       ]

with open (filepath,"w",encoding='utf-8')as outfile:
    writer = csv.writer(outfile,lineterminator='\n')
    writer.writerows(lst)

print('end of file')
