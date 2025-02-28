from math import *
import random
Q = False
#Borosilicate glass BK7
A = 1.5046
B = 0.00420 * 10**-12
landa=[500 , 532 , 604 , 670 , 689 , 709, 520]
def isGood(x):
    o = 0
    s= ['0','1','2','3','4','5','6','7','8','9','.']
    for i in x :
        if(i=='.'):
            o+= 1
        k =False
        for j in s :
            if(i==j):
                k=True
        if(not k):
            return 0
    if(o<=1):
        return 1
    else:
        return 0
def isGoodint(x):
    s= ['0','1','2','3','4','5','6','7','8','9']
    for i in x :
        k =False
        for j in s :
            if(i==j):
                k=True
        if(not k):
            return 0
    return 1
def partA():
    l=input("Choose laser number :")
    if(not isGoodint(l) or l ==''or int(l)<=0 or int(l)>=8):
        if(l=="exit"):
            return 0
        else :
            print("Invalid input Try again")
            return 1
    else:
        l=int(l)
        print(str( round(100*(0.01*round(-3.5+7*random.random()) + round(10000*landa[l-1]*1e-9*2.17/(1e-5))/100 ))/100 )+"cm")
        return 1
    
def partB():
    ok = False
    while(not ok):
        a = input("alpha :")
        if(a=="exit"):
            return 0
        if(not isGood(a)):
            print("Invalid input Try again")
        elif(float(a)<90 and float(a)>-90):
            ok = True
        else:
            print("Invalid input Try again")
    ok = False
    a = 0.1*int(10*float(a)) * pi / 180 
   # while(not ok):
      #  th = input("theta (deg) :")
       # if(th=="exit"):
       #     return 0
       # if(not isGood(th) or th%5 > 0 or th<5 or th>=90):
       #     print("Invalid input Try again/n")
       # else:
       #     ok = True
    #th = int(th)* pi / 180
    th = 30 * pi / 180
    ok = False
    while(not ok):
        l = input("Choose the laser number :")
        if(l=="1"or l=="2"or l=="3"or l=="4"or l=="5"or l=="6"or l=="7"):
            ok=True
        elif(l=="exit"):
            return 0
        else:
            print("Invalid input Try again")
    n = A+B/((10**-9)*landa[int(l)-1])**2
    j = sin(2*th) * (n**2-(sin(a))**2)**0.5 - sin(a)*cos(2*th)
    if(j>1):
        print("Total internal reflection was observed")
        return 1
    else:
        ph = asin(j)
        D = -2*th+a+ph
        print("D = "+str(0.001*round(1000*D*180/pi))[0:6])
        return 1

print("Virtual Exp 1 - summer 1401")
while(True):
    part = input("part A or B :")
    if(part == "A"or part=="a"):
        while(partA()):
            #nothing
            w=1
    elif(part=="B"or part == "b"):
        while(partB()):
            #nothing
            w=1
    else:
        print("Invalid input Try again:")
