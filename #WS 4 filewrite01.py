# WS 4 filewrite01 หมายเหตุ: \n คือรหัสคำสั่งขึ้นบรรทัดใหม่(New Line)

data = '1 hello,Kobkiat กอบเกียรติ 123\n'
lines = ['2 hi,Nan\n','This is my data file']

filepath = 'myfile.txt'
f1 = open(filepath,'w',encoding ='utf-8')

f1.write(data)
f1.writelines(lines)
f1.close()
