# WS12 fileread with try 01


filepath = 'myfiletest44.txt'
try:
    with open(filepath,'r',encoding ='utf-8') as f1: # เปิดไฟล์โดยใช้ f1 เป้นตัวอ้างอิง
        for line in f1: # เปิดไฟล์โดยใช้ f1 เป้นตัวอ้างอิง
            print(line)  #display data
except Exception as e: # ใช้แม่ข่าย(Exception)ในการทำงานแทนตัวลูกข่าย(IOError) ก็ได้
    print(e)   

print('end of file')
