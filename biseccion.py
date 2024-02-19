import math

def biseccion(f, a, b, tol):
    """
    Encuentra la raíz de la función f en el intervalo [a, b] usando el método de bisección
    y continúa hasta que la condición de parada basada en la tolerancia se cumpla.

    Parámetros:
    - f: función para la cual se busca la raíz.
    - a: límite inferior del intervalo.
    - b: límite superior del intervalo.
    - tol: tolerancia, criterio de parada basado en la precisión deseada, expresada en decimales.

    Imprime:
    - Número de iteraciones.
    - Error estimado en cada iteración después de la primera.

    Retorna:
    - La aproximación de la raíz y el error.
    """
    if f(a) * f(b) >= 0:
        print("El método de bisección falla debido a que f(a) * f(b) no es menor que 0.")
        return None
    
    iteracion = 0
    c = a
    error = float('inf')  # Inicializa el error a infinito
    while (b - a) / 2 > tol:
        c_previo = c
        c = (a + b) / 2
        iteracion += 1
        if iteracion > 1:
            error = abs((c - c_previo)/c)
            print(f"Iteración {iteracion}: valor actual = {c}, error = {error:.8f}")
        else:
            print("BISECCION")
            print(f"Iteración {iteracion}: valor actual = {c}")
        if f(c) == 0 or error < tol:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    print(f"Raíz encontrada: {c} en {iteracion} iteraciones con un error final de {error:.8f}")
    print("")
    return c, error
