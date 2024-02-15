import sympy as sp

def evaluar_funcion(func_sympy, x_val):
    x = sp.symbols('x')
    func_evaluada = func_sympy.subs(x, x_val)
    return float(func_evaluada)

def integracion_numerica(func_sympy, a, b, n):
    h = (b - a) / n
    resultado = 0
    for i in range(n):
        x_val = a + i * h
        resultado += evaluar_funcion(func_sympy, x_val)
    resultado *= h
    return resultado

# Test de la función de integración numérica
def test_integracion_numerica():
    x = sp.symbols('x')
    func = x*(x**2+1)**(1/2)  # Definimos la función para el test
    a = 0  # Límite inferior
    b = 1  # Límite superior
    n = 4  # Número de subintervalos
    
    # Calculamos la aproximación numérica
    resultado = integracion_numerica(func, a, b, n)
    
    # Calculamos el valor real de la integral
    integral_exacta = sp.integrate(func, (x, a, b))
    valor_real = float(integral_exacta.evalf())
    
    # Calculamos el error relativo
    error = abs((valor_real - resultado) / valor_real)
    
    print(f"La aproximación de la integral con {n} subintervalos es: {resultado:.6f}")
    print(f"El valor real de la integral es: {valor_real:.6f}")
    print(f"El error relativo es: {error:.6f}")

# Ejecutar el test automáticamente
if __name__ == "__main__":
    test_integracion_numerica()
