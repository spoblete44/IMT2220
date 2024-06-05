import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# Dibujar los puntos criticos calculados en el ejercicio anterior en la grafica de la funcion f(x,y) = x^2 + y^2 
# en el intervalo [-10,10]x[-10,10]
# para ello, primero genero los puntos del intervalo
# Dibujar los puntos criticos que calculamos para cada funcion como un marker en la grafica de contorno
# para ello, primero genero los puntos del intervalo
x = np.linspace(-30,30,100)
y = np.linspace(-30,30,100)

pt_x = (3 + math.sqrt(73)) / 8
pt_x2 = (3 - math.sqrt(73)) / 8

# ahora genero la malla de puntos
X,Y = np.meshgrid(x,y)

# ahora calculo los valores de la funcion en cada punto
Z1 = X**2 + Y**2
Z2 = X**2 - Y**2
Z3 = X**4 - X**3 - 2*X**2 + np.abs(Y)

# ahora dibujo la grafica
fig = plt.figure()
ax = fig.add_subplot(111)
ax.contour(X,Y,Z1)
ax.scatter([0],[0],color='red')
ax.scatter([pt_x],[0],color='red')
ax.scatter([pt_x2],[0],color='red')

plt.show()

