import numpy as np

def f(x):
    # Define la función que deseas integrar
    return x*((x**2+1)**(1/2))  # Ejemplo: f(x) = sin(x)

def trapezoidal_rule(a, b, n):
    # Calcula la aproximación de la integral definida usando el método del trapecio
    h = (b - a) / n
    integral_approx = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_i = a + i * h
        integral_approx += f(x_i)
    integral_approx *= h
    return integral_approx

def relative_error(true_value, approx_value):
    # Calcula el error relativo
    return np.abs((true_value - approx_value) / true_value)

# Ejemplo de uso
a = 0  # Límite inferior
b = 1  # Límite superior
n = 4 # Número de subintervalos

true_integral_value = 1  # Valor real de la integral (calculado analíticamente)
approx_integral_value = trapezoidal_rule(a, b, n)
error = relative_error(true_integral_value, approx_integral_value)

print(f"Aproximación de la integral: {approx_integral_value:.6f}")
print(f"Error relativo: {error:.6f}")

# Unit tests
def test_trapezoidal_rule():
    assert np.isclose(trapezoidal_rule(a, b, n), true_integral_value, rtol=1e-6)

def test_relative_error():
    assert np.isclose(relative_error(true_integral_value, approx_integral_value), error, rtol=1e-6)

if __name__ == "__main__":
    test_trapezoidal_rule()
    test_relative_error()
    print("Unit tests passed successfully!")
