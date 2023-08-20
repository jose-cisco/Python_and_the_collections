#if_name

def calArea(len):
    area = len*len
    return area

#main program โปรแกรมหลัก

if __name__ == '__main__':
    len    = 3
    a      = calArea(len)
    print('Area=',a)
