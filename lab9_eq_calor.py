

#Importar librerias necesarias 

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Defino las constantes que usarán durante todo el Problema

k = 0.6 # [W/m*K] --- Conductividad termica
c = 840 # [J/kg*K] --- Calor especifico
L = 0.2 # [m] --- Espesor
T0 = 273 # [K] --- Temperatura en x=0
TL = 298 # [K] --- Temepratura en x=L

M = 10 # [#] --- Numero de nodos

"""# Ecuación Diferencial

La ecuacion del calor es

$$ \frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2} $$

En el estado estacionario la temperatura no cambia con el tiempo, es decir que $ \partial T/ \partial t = 0$ 
$$ \alpha \frac{\partial^2 T}{\partial x^2}  = 0$$

# Aproximacion usando diferencias finitas

Aproximando la segunda derivada espacial de la temperatura en el punto $x$ con diferencias finitas centradas se obtiene:

$$\frac{\partial^2 T}{\partial x^2} \approx 
\frac{T(x+h)-2T(x)+T(x-h)}{h^2}$$

Reemplazando en la ecuación de calor estacionaria

$$\alpha \frac{T(x+h)-2T(x)+T(x-h)}{h^2} = 0$$

$$T(x+h)-2T(x)+T(x-h) = 0$$

$$T(x) = \frac{T(x+h)+T(x-h))}{2}$$

Lo anterior, como se puede evidenciar también en las ecuaciones del libro (2-17) y Ec. (5-11).
"""

# Defino el espacio

x = np.linspace(0, L, M)

# vector de T 
T = np.zeros(np.shape(x))

# condiciones de frontera en T

T[0] = T0
T[-1] = TL

# Solucion - Diferencias Finitas

#Para poder aplicar ecuaciones finitas debo iterar varias veces para poder ver estado estacionario en todos los puntos

#Elijo 100 repiticiones arbitrariamente (este valor se puede variar)

for j in range(100):
    for i in range(1,len(T)-1):


         #Temperatura como función de la posición para el  estado estacionario 

        # Solo se actualiza la temperatura de los nodos interiores (por definición)
        # Aproximacion de Diferencias Finitas

        T[i] = (T[i-1]+T[i+1])/2

# BONO : Gráfica de Temperatura como función de la posición para el  estado estacionario

fig, ax = plt.subplots()

#Perfil de temperatura

ax.plot(x, T, '.-') 

#Condiciones Frontera
#* para definir puntos extremos 

ax.plot([x[0],x[-1]], [T[0],T[-1]], '*',  ms=12) 

#set info plot

ax.grid()
ax.set_xlabel("c [°K]")
ax.set_ylabel("T [°K]")

"""**BONO: ANÁLISIS DE RESULTADOS**

En el estado estable el perfil de temperatura es lineal, acorde a lo que se espera de un material uniforme con temperatura diferente en los bordes

Este resultado se puede corroborar también resolviendo analíticamente la ecuacion diferencial

$$\frac{\partial^2 T}{\partial x^2} = 0$$

Donde la forma general de la solución es
$$T(x) = c_1 + c_2x$$

Teniendo en cuenta las condiciones de frontera
$$T(x=0) = T_0 \quad\Rightarrow\quad c_1=T_0$$

$$T(x=L) = T_L \quad\Rightarrow\quad c_2=\frac{T_L-T_0}{L}$$

La solución particular es
$$T(x) = T_0 + \frac{T_L-T_0}{L}x$$
con lo que se  corrobora lo que se ve en la gráfical del perfil lineal de temperatura y los valores en los bordes. 
"""
