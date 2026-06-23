from math import pi, e , sin , sqrt ,tanh

import random

H01 = 2400
H02 = 2000

k = 2 * pi / 2500
t = 2 * pi / 2900
  
xC1 = 3500
yC1 = 900
yC2 = 1100
xC2 = 200

a = 0.0375
b = 0.03

r3min = 480
r3max = 520

a1=  0.003
a2 = 0.003
h1min = 0

xmin = 0
xmax = 4000
ymin = 0
ymax = 5000
a3 = 80
xCrud = 270
yCrud = 4680
Rrud = 500
Crud = 24

def height(x,y):
    #kooh 1
    r1 = sqrt((x-xC1)**2 + (y-yC1)**2)
    h1 = H01 -a1*( r1**2 )
    if(h1 < h1min):
        h1 = 0


    #kooh 2
    r2 = sqrt((x-xC2)**2 + (y -yC2)**2)
    h2 = H02 * e**(-a2 * r2) + a* (x-xC2) + b * (y-yC2)
    if(h2 < 0):
        h2 = 0
    #rud

    r3 = sqrt((x-xCrud)**2 + (y -yCrud)**2)
    h3 = 0
    if(r3 > r3min and r3 < r3max):
        h3 = a3 * (tanh(-r3 + Rrud - Crud) + tanh(r3-Rrud - Crud))

    h = int(round(h1 + h2 + h3 + 70*sin(k*x + t*y) ))
    return h

while(True):
    x = input("insert x (m):")
    try :
        x= round(float(x),-1)
    except :
        print("\nWrong input\n")
        exit
    if(x>xmax or x<xmin):
        print("\nOut of range\n")
        exit

    y = input("insert y (m):")

    try :
        y= round(float(y),-1)
    except :
        print("\nWrong input\n")
        exit

    if(y<ymin or y > ymax):
        print("\nOut of range\n")
        continue
    h = height(x,y)
    if(h < 2200):
        print("h is " + str(h) + " (m)")
    else :
        print("\nVELAM KON :_( !\n")
    #RASME KHUTUTE HAM ERTEFA
    
