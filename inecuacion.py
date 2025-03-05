import numpy as np
import matplotlib.pyplot as plt

# Definir funciones de las restricciones
def restriccion1(a):
    return (120 - 2*a) / 3

def restriccion2(a):
    return (150 - 3*a) / 2

# Valores de A (0 a 60, ya que es el máximo encontrado)
a_vals = np.linspace(0, 60, 500)

# Calcular B en función de A para cada restricción
b_vals_1 = restriccion1(a_vals)
b_vals_2 = restriccion2(a_vals)

# Configuración del gráfico
plt.figure(figsize=(10, 7))

# Graficar las restricciones
plt.plot(a_vals, b_vals_1, label="2A + 3B ≤ 120", color="blue")
plt.plot(a_vals, b_vals_2, label="3A + 2B ≤ 150", color="green")

# Rellenar la región factible
plt.fill_between(a_vals, 
                 np.minimum(b_vals_1, b_vals_2), 
                 0, 
                 where=(b_vals_1 >= 0) & (b_vals_2 >= 0), 
                 color='gray', alpha=0.3)

# Etiquetas y título
plt.xlabel('Cantidad de A')
plt.ylabel('Cantidad de B')
plt.title('Región Factible del Problema de Optimización')
plt.legend()
plt.grid(True)

# Limitar los ejes
plt.xlim(0, 60)
plt.ylim(0, 80)

# Mostrar gráfico
plt.show()
