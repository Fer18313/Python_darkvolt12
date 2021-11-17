# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:13:06 2021

@author: Fernando Sandoval
"""
import numpy as xls


def jacobi(A, b, tolerance, n):
    
    x = xls.zeros_like(b, dtype=xls.double)
    T = A - xls.diag(xls.diagonal(A))
    for k in range(n):
        x_old  = x.copy()
        x[:] = (b - xls.dot(T, x)) / xls.diagonal(A)
        if xls.linalg.norm(x - x_old, ord=xls.inf) / xls.linalg.norm(x, ord=xls.inf) < tolerance:
            break
            
    return x
"""
INGRESO DE VALORES PARA LA 
FUNCION DE JACOBI.

""" 
tolerance = 1e-7
X = xls.array([[6,1,2],[1,-1,3],[3,8,1]])
b = ([3,3,2])
m = 3 #variables
xp = xls.zeros(m)
n = 400
x = jacobi(X,b,tolerance,n) 
print(x)



# GAUSS SEIDEL

F_0 = lambda x,y,z: (6*x+y+2*z)/20
F_1 = lambda x,y,z: (3*x+8*y+z)/20
F_2 = lambda x,y,z: (x-y+3*z)/20

x0 = 3
y0 = 3
z0 = 2
counter = 1

e = 1e-8

print('\nCount\tx\ty\tz\n')

cons = True

while cons:
    x1 = F_0(x0,y0,z0)
    y1 = F_1(x1,y0,z0)
    z1 = F_2(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(counter, x1,y1,z1))
    e1 = abs(x0-x1);
    e2 = abs(y0-y1);
    e3 = abs(z0-z1);
    
    counter += 1
    x0 = x1
    y0 = y1
    z0 = z1
    
    cons = e1>e and e2>e and e3>e

print('\nsolucion: x=%0.3f, y=%0.3f and z = %0.3f\n'% (x1,y1,z1))
         
            
            
            
    
    
    
    