# WS 5 READING FILE

filepath = 'myfile.txt'
f1 = open(filepath,'r',encoding ='utf-8') # mode = 'r' (read)

while True:
    line = f1.readline()
    if len(line):
        print(line)
    else :
        break

print(line)
f1.close()
