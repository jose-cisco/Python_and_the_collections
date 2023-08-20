# DEF WEIGHT

w1 = float(input('Enter Weight(kg):'))
w2 = float(input('Enter Weight(kg):'))
def Weight(w):
    sc_1  = w1 * 10
    sc_2  = w2 * 20
    print('Service Charge for {} kg = {} THB'.format(w1,sc_1))
    print('Service Charge for {} kg = {} THB'.format(w2,sc_2))   
    return sc_1,sc_2

#Main Program
sc_1 = Weight(w1)
sc_2= Weight(w2)
a = (sc_1+sc_2)
print('a = {}'.format(a))
