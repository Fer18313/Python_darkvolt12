## FERNANDO JAVIER SANDOVAL RUBALLOS
## CARNE: 18313

import numpy as np
from pylab import *
import scipy.interpolate as si

#################################################################################################
##                                          PARTE 1                                            ##
##       VOLUMEN 
 
## COODERNADAS X 

## IMPORTANTE QUE 3.04 SEA EL COMIENZO DEL SEGUNDO ARRAY, ASI LOGRAMOS UNIR
x0 = [0, 0.6, 1.4, 2, 2.8, 3.04]
x1 = [3.04, 3.5, 4.58, 5.09, 5.69, 6.17, 6.65, 7.18]

## COORDENADAS Y 

y0 = [2.03, 3.01, 3.54, 3.71, 4, 4.33]
y1 = [4.29, 3.89, 4.1, 4.49, 5.18, 5.8, 6.21, 6.57]

plot(x0,y0, 'o')
plot(x1,y1, 'o')

get_ipython().set_next_input('tck1 = si.splrep');get_ipython().run_line_magic('pinfo', 'si.splrep')

tck1 = si.splrep
tck1 = si.splrep

get_ipython().set_next_input('tck2 = si.splrep');get_ipython().run_line_magic('pinfo', 'si.splrep')

tck2 = si.splrep
tck2 = si.splrep

tck1 = si.splrep(x0, y0)
tck2 = si.splrep(x1, y1)

y_sd = linspace(min(x0), max(x0), 100)
y_sd2 = linspace(min(x1), max(x1), 100)
x_space = si.splev(tck = tck1, x = y_sd)
x_space2 = si.splev(tck = tck2, x = y_sd2)

plot(x_space, y_sd)
plot(x_space2, y_sd2)

x_inter = x_space**2
x_inter2 = x_space2**2
plot(x_inter, y_sd)
plot(x_inter2, y_sd2)

tckInt = si.splrep(y_sd, x_inter)
tckInt2 = si.splrep(y_sd2, x_inter2)
v_0 = pi*si.splint(a = 0, b = 3.04, tck = tckInt)
v_1 = pi*si.splint(a = 3.04, b = 7.18, tck = tckInt2)
vol = v_0+v_1
print('volumen: ',vol)
#################################################################################################
##                                        PARTE 2                                              ##

## AREA SUPERFICIAL 

yprev1 = si.splder(tck1)
yprev2 = si.splder(tck2)

y_rdy = si.splev (tck = yprev1, x = y_sd)
y_rdy2 = si.splev (tck = yprev2, x = y_sd2)


y_rdy = y_rdy**2
y_rdy2 = y_rdy2**2

y_inter = np.sqrt(1+y_rdy)
y_inter2 = np.sqrt(1+y_rdy2)

tck_inter = si.splrep(y_sd, y_inter)
tck_inter2 = si.splrep(y_sd2, y_inter2)

a_0 = 2*pi*si.splint(a = 0, b = 3.04, tck = tck_inter)
a_1 = 2*pi*si.splint(a = 3.04, b = 7.18, tck = tck_inter2)
surf_area = a_0 + a_1
print ('Area Superficial: ',surf_area)


