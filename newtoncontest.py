import sympy as sp

def newton_raphson_sympy(func, x0, tol, max_iter=100):
    """
    Encuentra la raíz de una función usando el método de Newton-Raphson.

    Parámetros:
    - func: La función para la cual se busca la raíz, dada como una expresión de sympy.
    - x0: Aproximación inicial a la raíz.
    - tol: Tolerancia para el criterio de parada basado en el error relativo.
    - max_iter: Número máximo de iteraciones.

    Retorna:
    - La aproximación a la raíz de la función si se encuentra dentro de las iteraciones dadas.
    """
    x = sp.symbols('x')  # Define el símbolo x para derivar y evaluar la función
    f = func
    f_deriv = sp.diff(f, x)  # Deriva la función automáticamente

    f_lamb = sp.lambdify(x, f, 'numpy')  # Prepara la función para evaluación numérica
    f_deriv_lamb = sp.lambdify(x, f_deriv, 'numpy')  # Prepara la derivada para evaluación numérica

    xn = x0
    for n in range(max_iter):
        fxn = f_lamb(xn)
        dfxn = f_deriv_lamb(xn)
        if abs(dfxn) < tol:
            print("Derivada muy cercana a cero. El método podría no converger.")
            return None
        xn_next = xn - fxn / dfxn
        if n > 0:  # Calcula el error relativo desde la segunda iteración
            error = abs(xn_next - xn) / abs(xn_next)
            print(f"Iteración {n}: x = {xn_next:.8f}, error = {error:.8f}")
            if error < tol:
                print(f"Convergencia alcanzada en iteración {n}.")
                return xn_next
        else:
            print(f"Iteración {n}: x = {xn_next:.8f}")  # Primera iteración sin comparar error
        xn = xn_next
    
    print("Máximo de iteraciones alcanzado. Puede que no se haya encontrado la convergencia.")
    return xn

# Test del algoritmo con una función específica
if __name__ == "__main__":
    x = sp.symbols('x')
    func = sp.log(x) + x**2 - 4  # Función correcta
    x0 = 1.5  # Aproximación inicial

    print(f"Buscando la solucion de la función = {func} ...")
    root = newton_raphson_sympy(func, x0, 0.01)
    print(f"Raíz encontrada: {root}")
