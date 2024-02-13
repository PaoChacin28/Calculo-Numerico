from sympy import symbols, sympify, diff

def newton_raphson_convergencia(f_sym, x0, tol, max_iter):
    """
    Método de Newton-Raphson con impresiones detalladas de cada iteración.
    """
    x = symbols('x')
    df_sym = diff(f_sym, x)  # Derivada de la función
    ddf_sym = diff(df_sym, x)  # Segunda derivada de la función
    
    f = lambda x_val: f_sym.subs(x, x_val).evalf()
    df = lambda x_val: df_sym.subs(x, x_val).evalf()
    ddf = lambda x_val: ddf_sym.subs(x, x_val).evalf()
    
    # Calcular el criterio de convergencia
    criterio = (f(x0) * ddf(x0)) / (df(x0) ** 2)
    print("")
    if criterio >= 1:
        print("El criterio de convergencia sugiere que el método puede no converger.")
        return None
    else:
        print("El criterio de convergencia sugiere que el método debería converger.")
    
    print("")
    print("{:^60}".format("MÉTODO DE NEWTON-RAPHSON"))
    print("{:^10} {:^20} {:^20}".format("Iteración", "Aproximación", "Error"))
    
    xn = x0
    error = tol + 1  # Asegurar que el bucle comience
    i = 1  # Contador de iteraciones
    
    while error > tol and i <= max_iter:
        fxn = f(xn)
        dfxn = df(xn)
        if dfxn == 0:
            print("Derivada nula en la iteración. El método no puede continuar.")
            return None
        xn1 = xn - fxn/dfxn  # Nueva aproximación
        error = abs(xn1 - xn)
        print("{:^10} {:^20.10f} {:^20.10f}".format(i, xn1, error))
        
        xn = xn1
        i += 1
    
    if error <= tol:
        print("")
        print(f"Solución encontrada: x = {xn1:.10f} con un error de {error:.10f} después de {i-1} iteraciones.")
    else:
        print("Se alcanzó el máximo de iteraciones sin converger a la solución deseada.")

# Solicitar entrada del usuario
funcion_usuario = input("Ingresa tu función en términos de x: ")
x0 = float(input("Ingresa el valor inicial x0: "))
tol = float(input("Ingresa el margen de error (tolerancia), usa punto para decimales: "))
max_iter = int(input("Ingresa el número máximo de iteraciones: "))

# Convertir la entrada a una expresión sympy
f_sym = sympify(funcion_usuario)

# Llamar al método de Newton-Raphson con impresiones detalladas
newton_raphson_convergencia(f_sym, x0, tol, max_iter)
