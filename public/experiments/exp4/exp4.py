from math import pi , sin , cos , sqrt
g = 9.81
m = 1.5
q = 0.3261
E = 31.5
th = 40 * (pi/180)
w = 7.85
H = 32


hmin =0
hmax = 20

v0xmin = -20
v0xmax = 20

v0ymin = -20
v0ymax = 20

v0zmin = -20
v0zmax = 20

E0xmin = -15
E0xmax = 15

E0ymin =-15
E0ymax =15

E0zmin =-15
E0zmax =15


while(True):
    h_OK = False
    v0x_OK = False
    v0y_OK = False
    v0z_OK = False
    E0x_OK = False
    E0y_OK =False
    E0z_OK =False

    while(not h_OK):
        h = input("Insert h(m):")
        if(h=="x"):
            break
        try :
            h = float(h)
        except :
            continue
        if(h>=hmin and h<= hmax):
            h_OK = True
    while(not v0x_OK): 
        v0x =input("Insert v0x(m/s):")
        if(v0x=="x"):
            break
        try :
            v0x = float(v0x)
        except :
            continue
        if(v0x >= v0xmin and v0xmax >= v0x):
            v0x_OK = True
        

    while(not v0y_OK):
        v0y =input("Insert v0y(m/s):")
        if(v0y=="x"):
            break
        try :
            v0y = float(v0y)
        except :
            continue
        if(v0y >= v0ymin and v0ymax >= v0y):
            v0y_OK = True
        

    while(not v0z_OK):
        v0z =input("Insert v0z(m/s):")
        if(v0z=="x"):
            break
        try :
            v0z = float(v0z)
        except :
            continue
        if(v0z >= v0zmin and v0zmax >= v0z):
            v0z_OK = True
        

    while(not E0x_OK):
        E0x =input("Insert E0x(V/m):")
        if(E0x=="x"):
            break
        try :
            E0x = float(E0x)
        except :
            continue
        if(E0x <= E0xmax and E0x >= E0xmin):
            E0x_OK =True
        

    while(not E0y_OK):
        E0y =input("Insert E0y(V/m):")
        if(E0y=="x"):
            break
        try :
            E0y = float(E0y)
        except :
            continue
        if(E0y <= E0ymax and E0y >= E0ymin):
            E0y_OK =True
        
    while(not E0z_OK):
        E0z =input("Insert E0z(V/m):")
        if(E0z=="x"):
            break
        try :
            E0z = float(E0z)
        except :
            continue
        if(E0z <= E0zmax and E0z >= E0zmin):
            E0z_OK =True
        
    G = g - (q/m)*(E0z+E*cos(th))
    L = H - h
    if(v0z > sqrt(2*L*G)):
        f = 2*sqrt(v0z**2 - 2*L*G)
    else :
        f = 0
    T=(v0z+sqrt(v0z**2 + 2*h*G))/G - f/G
    X=q*E*sin(th)*(1-cos(w*T))/(m*w**2) + v0x * T + q*E0x * T**2 / (2*m)
    Y=(q*E*sin(th)/(m*w))*(T-sin(w*T)/w) + v0y * T + q*E0y * T**2 / (2*m)
    print("X = " + str(round(X,4)) + " (m)")
    print("Y = " + str(round(Y,4)) + " (m)")
    print("T = " + str(round(T,4)) + " (s)")
