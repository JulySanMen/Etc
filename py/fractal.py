import numpy as np
import matplotlib.pyplot as plt

# Definir la función de Mandelbrot
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    return n

# Parámetros para generar el fractal
def generar_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    fractal = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            c = r1[i] + r2[j]*1j
            fractal[i, j] = mandelbrot(c, max_iter)
    
    return fractal

# Definir el tamaño de la imagen y el rango del plano complejo
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 256

# Generar el fractal
fractal = generar_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

# Graficar el fractal usando matplotlib
plt.imshow(fractal.T, extent=[xmin, xmax, ymin, ymax], cmap='twilight_shifted')
plt.colorbar()
plt.title("Conjunto de Mandelbrot")
plt.show()