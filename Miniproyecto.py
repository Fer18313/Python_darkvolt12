
"""
Created on Sun Aug  8 11:16:11 2021
@author: Fernando Sandoval
#CARNE: 18313
#CLASE: METODOS NUMERICOS
"""
"""
------------------------------------------------------------------------------------------------------------
                              ____________NEWTON_RAPHSON_METHOD______________
                                ___________FRACTAL_GENERATION____________
------------------------------------------------------------------------------------------------------------
"""
"""
IMPORT---LIBRARIES
"""
import numpy as xls
import matplotlib.pyplot as kod
from matplotlib.colors import ListedColormap
"""
Never-changing variables
"""
RGB_lights_like_titkok = ['r', 'g', 'b', 'y']

"""
Change the tolerance allowed here:
"""
tolerance = 1.e-7

"""
TO RUN THIS CODE AND GENERATE ANOTHER
FRACTAL IMAGE, YOU MUST INPUT THE 
FOLLOWING VARIABLES: 
"""
F = lambda k: k**3 - 1 
Fp = lambda k: 3*(k)**2
N = 400

"""
Newton Raphson method code, this
retrieves the roots for the function
"F"

"""

def NEWTON_RAPHSON_METHOD(k_0, F, Fp, Iterations=500):
    k = k_0
    for i in range(Iterations):
        dk = (F(k)/Fp(k))
        if abs(dk) < tolerance:
            return k
        k -= dk
    return False


"""
This is the main code, here we generate
the graphical image of the fractal, 
taking as the main computing element
the Newton Raphson method.
"""

"""
TO SEE MORE OF THE IMAGE YOU MUST CHANGE THE DOMAIN, 
IF APPLICABLE, YOU CAN ALSO CHANGE THE N.
"""
def FRACTAL_GEN(F, Fp, n=300, D=(-1, 1, -1, 1)):
    R = []
    m_grid = xls.zeros((n, n))
    def R_INDEX_COUNT(XOR, RAND):
        try:
            return xls.where(xls.isclose(R, RAND, atol=tolerance))[0][0]
        except IndexError:
            R.append(RAND)
            return len(R) - 1
    x_0, x_1, y_0, y_1 = D
    for ix, x in enumerate(xls.linspace(x_0, x_1, n)):
        for iy, y in enumerate(xls.linspace(y_0, y_1, n)):
            k_0 = x + y*1j
            RAND = NEWTON_RAPHSON_METHOD(k_0, F, Fp)
            if RAND is not False:
                xanax = R_INDEX_COUNT(R, RAND)
                m_grid[iy, ix] = xanax
    num = len(R)
    if num > len(RGB_lights_like_titkok):
        vamp = 'hsv'
    else:
        vamp = ListedColormap(RGB_lights_like_titkok[:num])
    kod.imshow(m_grid, cmap=vamp, origin='lower')
    kod.axis('off')
    kod.show()
"""
Here we finalize the code by computing 
according to the inputs.
"""
print("FRACTAL IMAGE GENERATING...")
FRACTAL_GEN(F, Fp, N)
print("FRACTAL IMAGE GENERATED.")