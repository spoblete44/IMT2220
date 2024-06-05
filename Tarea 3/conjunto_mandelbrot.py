import numpy as np
import matplotlib.pyplot as plt


def imshow_conjuntomandelbrot(V, res, K):
    x = np.linspace(V[0], V[1], res)
    y = np.linspace(V[2], V[3], res)
    X, Y = np.meshgrid(x, y)
    puntos = X + 1j * Y
    x = np.zeros_like(puntos)
    puntos_del_conjunto = np.ones_like(puntos, dtype=bool)
    
    for k in range(K):
        x[puntos_del_conjunto] = x[puntos_del_conjunto]**2 + puntos[puntos_del_conjunto]
        puntos_del_conjunto[np.abs(x) > 2] = False

    plt.imshow(puntos_del_conjunto, extent=(V[0], V[1], V[2], V[3]), origin='lower', cmap='hot')
    plt.title('Conjunto de Mandelbrot')
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.colorbar()
    plt.show()

V = [-2.5, 1.5, -2, 2]
imshow_conjuntomandelbrot(V, res=1000, K=100)