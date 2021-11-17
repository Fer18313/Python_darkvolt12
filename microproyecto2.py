"""
Created on Mon Oct  4 18:43:50 2021

@author: Fernando Sandoval
Carne: 18313
FECHA: 10/04/2021

"""


## IMPORTED LIBRARIES NEEDED TO COMPUTE SOME TERMS

from pylab import *
import numpy

## FUNCTION DEFINITIONS NEEDED TO SOLVE PROBLEMS ACCORDING TO 
## NUMERICAL METHODS 1, UNIDIMENSIONAL DERIVATIVES WORKSHEET

def derivative_central(y,h):
    var_0=len(y)
    res=zeros(var_0)
    for i in range(1,var_0-1):
        res[i]= (y[i+1]-y[i-1])/(2*h)
    return res

def richardson_method(y,h):
    var_0=len(y)
    res=zeros(var_0)
    for i in range(2,var_0-2):
        res[i]=  (4/3)*(y[i+1]-y[i-1])/(2*h)-(1/3)*(y[i+2]-y[i-2])/(4*h)
    return res

def derivative_forward(y,h):
    var_0=len(y)
    res=zeros(var_0)
    for i in range(0,var_0-1):
        res[i]= (y[i+1]-y[i])/h
    return res


                                    ## PROBLEMA 1
perimeter=250
x1=linspace(0,125,1000)
y1=((perimeter*x1)/2)-((x1**2)/2)-((3*pi*(x1**2))/16)
h1=0.125

res_0=derivative_forward(y1,h1)
res_1=derivative_central(y1,h1)
res_2=richardson_method(y1,h1)

RES=[(res_0,"Forward"),(res_1,"Central"),(res_2,"Richardson")]

for i, Res in enumerate(RES):
    res,me= Res
    figure(i)
    plot(x1,y1)
    plot(x1,res,"ro")
    grid()
    title(me)

AREA_0=numpy.where((res_2 < 0.1)&(res_2 > -0.1))
MAX_AREA=max(y1[AREA_0])


for i in range(0,len(x1)):
    if(y1[i]==max(y1[AREA_0])):
        test=i

x_coordinate=test/len(x1)*x1[len(x1)-1]
y_coordinate=perimeter/2-x_coordinate/2-(pi*x_coordinate)/4
x1=linspace(20,25,100)
y1=((perimeter*x1)/2)-((x1**2)/2)-((3*pi*(x1**2))/16)
plot(x1,y1)
print("")
print("PROBLEMA 1")
print("Longitud horizontal de la ventana: ",x_coordinate)
print("Longitud vertical de la ventana: ",y_coordinate)

                                ## PROBLEMA 2
                                
x = linspace(0.1,15,1000)
y = ((x+27)**2+(((8*x+216)/(x)))**2)**(0.5)

h = 0.0149

res_3=derivative_forward(y,h)
res_4=derivative_central(y,h)
res_5=richardson_method(y,h)

POP=[(res_3,"Forward"),(res_4,"Central"),(res_5,"Richardson")]

for i, Res in enumerate(POP):
    res,me= Res
    figure(i)
    plot(x,y)
    plot(x,res,"ro")
    grid()
    title(me)
    

AREA_1=numpy.where((res_5 < 0.1)&(res_5 > -0.1))
min_length=min(y[AREA_1])


x=linspace(11.5,12.5,100)
y=((x+27)**2+(((8*x+216)/(x)))**2)**(0.5)
plot(x,y)
x=12
y=((x+27)**2+(((8*x+216)/(x)))**2)**(0.5)

print("")
print("PROBLEMA 2")
print("Longitud más corta: ",min_length)

                                    ## PROBLEMA 3
g=9.81
ho=10
vo=20

x=linspace(0,pi/2,1000)

y=((vo**2)*cos(x)/g)*(sin(x)+((sin(x)**2)+((2*g*ho)/(vo**2)))**(0.5))
h=0.00157079

res_6=derivative_forward(y,h)
res_7=derivative_central(y,h)
res_8=richardson_method(y,h)

POP2=[(res_6,"Forward"),(res_7,"Central"),(res_8,"Richardson")]

for i, Res in enumerate(POP2):
    res,me= Res
    figure(i)
    plot(x,y)
    plot(x,res,"ro")
    grid()
    title(me)

HU=numpy.where((res_8 < 0.5)&(res_8 > -0.5))
MAX_D=max(y[HU])


for i in range(0,len(x)):
    if(y[i]==max(y[HU])):
        end=i
print("")
print("PROBLEMA 3")
print("lA MAXIMA DISTANCIA ES: ", MAX_D)                  
                        
                                ## PROBLEMA 4
x=linspace(0,4,1000)
y= 10*cos(pi*x)
h=0.004
coordinate=y

res_9=derivative_forward(y,h)
res_10=derivative_central(y,h)
res_11=richardson_method(y,h)


v= res_11
a= richardson_method(v,h)


POP3=[(res_9,"Forward"),(res_10,"Central"),(res_11,"Richardson")]

for i, Res in enumerate(POP3):
    res,me= Res
    figure(i)
    plot(x,y)
    plot(x,res,"ro")
    plot(x,a,"go")
    grid()
    title(me)

figure(i)
plot(x,coordinate)
plot(x,v,"ro")
plot(x,a,"go")
grid()
title("Position, Velocity, Acceleration" )

print("")
print("PROBLEMA 4")
print("")
AM=numpy.where((coordinate < 0.05)&(coordinate > -0.05))

for i in range(0,len(x)):
    if(y[i]==max(y[AM])):
        l=i
        
        
print("Inciso a) ")
MAX_v = v[AM]
print("Maxima velocidad: ", MAX_v)
t=[125/len(x)*x[len(x)-1],375/len(x)*x[len(x)-1],624/len(x)*x[len(x)-1],874/len(x)*x[len(x)-1]]
print("Tiempo en el cual el carro alcanza esta rapidez: ",t)

a_max_recorrido = coordinate[AM]
print("La posicion para la velocidad maxima: ",a_max_recorrido)

a_max= a[AM]
print("La aceleracion cuando la velocidad es maxima: ", a_max)

print("")
print("Inciso b) ")
AM2=numpy.where((v < 0.1)&(v> -0.1))
for i in range(0,len(x)):
    if(y[i]==max(y[AM2])):
        li=i
AM2=np.delete(AM2,1)
AM2=np.delete(AM2,4)

MAX_RECORRIDO = coordinate[AM2]

print("La posicion cuando la aceleracion es maxima: ", MAX_RECORRIDO)
MAX_V = v[AM2]
print("Rapidez maxima: ", MAX_V)




