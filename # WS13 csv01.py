# WS13 csv01
import csv
filepath = 'myfilecsv.txt'

row = [1,'กอบเกียรติ',25]

with open (filepath,"w",encoding='utf-8')as outfile:
    writer = csv.writer(outfile)
    writer.writerow(row)

print('done')
