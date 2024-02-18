import sympy as sp

def evaluar_funcion(func_sympy, x_val):
    x = sp.symbols('x')
    func_evaluada = func_sympy.subs(x, x_val)
    return float(func_evaluada)

def integracion_riemann(func_sympy, a, b, n):
    h = (b - a) / n
    resultado = (evaluar_funcion(func_sympy, a)*h)
    for i in range(1, n):
        x_val = a + i * h
        resultado += evaluar_funcion(func_sympy, x_val)
    resultado *= h
    # Calculamos el valor real de la integral
    x = sp.symbols('x')
    integral_exacta = sp.integrate(func_sympy, (x, 0, 1))
    valor_real = float(integral_exacta.evalf())
    # Calculamos el error relativo
    error_riemann = abs((valor_real - resultado) / valor_real)
    print(f"Valor real de la integral: {valor_real:.6f}")
    print(f"Riemann: Aproximación = {resultado:.6f}, Error relativo = {error_riemann:.6f}")
    return resultado, error_riemann

def integracion_trapecio(func_sympy, a, b, n):
    h = (b - a) / n
    resultado = (evaluar_funcion(func_sympy, a) + evaluar_funcion(func_sympy, b)) / 2
    for i in range(1, n):
        x_val = a + i * h
        resultado += evaluar_funcion(func_sympy, x_val)
    resultado *= h
    # Calculamos el valor real de la integral
    x = sp.symbols('x')
    integral_exacta = sp.integrate(func_sympy, (x, 0, 1))
    valor_real = float(integral_exacta.evalf())
    error_trapecio = abs((valor_real - resultado) / valor_real)
    print(f"Valor real de la integral: {valor_real:.6f}")
    print(f"Trapecio: Aproximación = {resultado:.6f}, Error relativo = {error_trapecio:.6f}")
    return resultado, error_trapecio

