# WS11.1 fileread with 01


filepath = 'myfiletest44.txt'
with open(filepath,'r',encoding ='utf-8') as f1: # เปิดไฟล์โดยใช้ f1 เป้นตัวอ้างอิง
    for line in f1: # เปิดไฟล์โดยใช้ f1 เป้นตัวอ้างอิง
        print(line)  #display data
    

print('done')
