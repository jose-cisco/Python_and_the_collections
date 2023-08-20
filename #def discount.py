#def discount

Price               = eval(input('Enter product price:'))
Disc_rate           = 5
def discount():
    Discount   = Price * (Disc_rate/100)
    Total_Net  = Price - Discount
    print('in discount Discount={} Total_net={}'.format(Discount,Total_Net))
    return Disc_rate #ขอแค่ให้มี return ตัวแปรก็พอ พอ return ตัวแปรแล้ว ตัวแปรจะเข้า discount แล้วไป main program เลย 

# Main Program
if __name__ == '__main__':
    discount() 
    
