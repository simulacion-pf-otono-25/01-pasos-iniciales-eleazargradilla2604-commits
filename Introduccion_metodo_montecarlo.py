#Introduccion metodo montecarlo
import numpy as np
import matplotlib.pyplot as plt

#limites de integracion
a = 0
b = 2

def funcion_a_integrar(x):
    return -x ** 2

N = 100000

x = np.random.uniform(a, b, N)
y = np.random.uniform(funcion_a_integrar(a),funcion_a_integrar(b),N)



n_bajo_curva =np.sum( y < funcion_a_integrar(x))
respuesta_de_integral = (b-a) * (funcion_a_integrar(b) - funcion_a_integrar(a)) * n_bajo_curva / N

plt.plot(x, y, 'o')
plt.plot(np.linspace(a,b,10),funcion_a_integrar(np.linspace(a,b,10)))
plt.show()

