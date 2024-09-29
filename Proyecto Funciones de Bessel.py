#Universidad del Valle de Guatemala
#Metodos Matematicos para la Fisica II. Profesora: Yasmin Portillo Chang.
#Proyecto Funciones de Bessel.
#---------------------------------------------------------------------#
#Integrantes:
#--Evelyn Fernanda López Peiro--21126
#--Pedro José Camposeco Ovalle--21360
#--Angel Josue Nij Culajay------21437
#---------------------------------------------------------------------#

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

#Definiendo la forma integral de la función de Bessel de primer tipo de aceurdo a la guia.
def bessel_jn(n, x):
    integrand = lambda theta: np.cos(x * np.sin(theta) - n * theta)
    result, _ = quad(integrand, 0, np.pi)
    return result / np.pi

#Definiendo la forma integral de la función de Bessel modificada de primer tipo de orden 0.
def bessel_i0(x):
    integrand = lambda theta: np.cosh(x * np.cos(theta)) 
    result, _ = quad(integrand, 0, np.pi)
    return result / np.pi

x_values = np.linspace(0, 20, 500)
colors = ['red', 'skyblue', 'orange', 'black', 'purple']
linestyles = ['-', '-', '-', '-', '--']

#-------------------------------------------------------------------------#
# Funciones de Bessel J_n(x)
plt.figure(figsize=(10, 6))
for n in range(5):  # Para n = 0, 1, 2, 3, 4
    jn_values = [bessel_jn(n, x) for x in x_values]
    plt.plot(x_values, jn_values, label=f'J_{n}(x)', color=colors[n], linestyle=linestyles[n])
    
plt.title('Funciones de Bessel de primer tipo J_n(x)')
plt.xlabel('x')
plt.ylabel('J_n(x)')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(0, 21, 2))
plt.xlim(0, 20)
plt.show()
#-------------------------------------------------------------------------#
#Función de Bessel modificada I_0(x)
plt.figure(figsize=(10, 6))
i0_values = [bessel_i0(x) for x in x_values]
plt.plot(x_values, i0_values, label='I_0(x)', color='red', linestyle= "--")
plt.title('Función de Bessel modificada de primer tipo I_0(x)')
plt.xlabel('x')
plt.ylabel('I_0(x)')
plt.legend()
plt.grid(True)
plt.ylim(0, 5)
plt.xlim(0, 5)
plt.show()
#-------------------------------------------------------------------------#
#Grafica conjunta J_n(x) y I_0(x)#
fig, ax1 = plt.subplots(figsize=(10, 6))
for n in range(5):  # Para n = 0, 1, 2, 3, 4
    jn_values = [bessel_jn(n, x) for x in x_values]
    ax1.plot(x_values, jn_values, label=f'J_{n}(x)', color=colors[n], linestyle=linestyles[n])
    
ax1.set_xlabel('x')
ax1.set_ylabel('J_n(x)', color='black')
ax1.grid(True)

ax2 = ax1.twinx()
i0_values = [bessel_i0(x) for x in x_values]
ax2.plot(x_values, i0_values, label='I_0(x)', color='blue', linestyle='-.')
ax2.set_ylabel('I_0(x)', color='blue')

plt.title('Funciones de Bessel J_n(x) y función de Bessel modificada I_0(x)')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
ax2.set_ylim(0,5)
ax2.set_xlim(0,5)
plt.xticks(np.arange(0, 21, 1))
plt.show()

