from math import e , sqrt
while(True):
    H = 3104
    Yc = 755
    Xc = 427
    a = 3.147e-5
    x = input("Select x(m):")
    try :
        x = round(int(x),-1)
    except :
        print("\nWrong input !\n")
        continue
    if (x<0 or x> 1000) :
        print("\nOut of range\n")
        continue
    y = input("Select y(m):")
    try :
        y = round(int(y),-1)
    except :
        print("\nWrong input !\n")
        continue
    if(y<0 or y>1000):
        print("\nOut of range\n")
        continue
    r = sqrt( (y-Yc)**2 + (x-Xc)**2 )
    h = H * e**(-a*r**2) + 30 - (x+y) * (3/200)
    print("h = " + str(int(h)) + " (m)")
