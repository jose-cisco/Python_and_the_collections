# WS10 filewrite with 01

data = '1 hello,Kobkiat กอบเกียรติ 123\n'
lines = ['2 hi,Nan\n','This is my data file']

filepath = 'myfiletest.txt'
with open(filepath,'w',encoding ='utf-8') as f1:
    f1.write(data)
    f1.writelines(lines)

print('done')
