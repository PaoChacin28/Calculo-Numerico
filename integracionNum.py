import numpy as np
import sympy as sp

# Función para evaluar la expresión ingresada por el usuario en x
def evaluar_funcion(func, x_val):
    x = sp.symbols('x')
    func_evaluada = func.subs(x, x_val)
    return float(func_evaluada)

# Solicitar al usuario que ingrese la función
funcion_usuario = input("Introduce la función a integrar (en términos de x): ")
func = sp.sympify(funcion_usuario)

# Entradas del usuario para los límites de integración y el número de subintervalos
a = float(input("Introduce el límite inferior de integración (a): "))
b = float(input("Introduce el límite superior de integración (b): "))
n = int(input("Introduce el número de subintervalos (n): "))

# Calcula la integral exacta usando integración simbólica
x = sp.symbols('x')
integral_exacta = sp.integrate(func, (x, a, b))

# Función para calcular la suma de Riemann por la izquierda
def suma_riemann(func, a, b, n):
    h = (b - a) / n
    suma = sum(evaluar_funcion(func, a + i * h) for i in range(n))
    return suma * h

# Cálculo de la suma de Riemann
resultado_aproximado = suma_riemann(func, a, b, n)
print(f"La aproximación de la integral con {n} subintervalos es: {resultado_aproximado:.6f}")

# Cálculo del error
valor_real = integral_exacta.evalf()
error = abs((valor_real - resultado_aproximado) / valor_real)
print(f"El valor real de la integral es: {valor_real:.6f}")
print(f"El error relativo es: {error:.6f}")
