import unittest
import sympy as sp
import math
from biseccion import biseccion
from newtonRaphson import newton_raphson_sympy
from integracionNumerica import integracion_riemann, integracion_trapecio

class TestNewtonRaphson(unittest.TestCase):
    def test_root_finding(self):
        x = sp.symbols('x')
        func = sp.log(x)+x**2-4
        root = newton_raphson_sympy(func, x0=1.5, tol=0.01)
        self.assertAlmostEqual(root, 1.8410, places=2, msg="La raíz encontrada no es precisa.")

    def test_convergence_failure(self):
        x = sp.symbols('x')
        func = x**2
        root = newton_raphson_sympy(func, x0=1.5, tol=0.01, max_iter=100)
        self.assertIsNone(root, "La función debería indicar una falla en la convergencia.")

class TestIntegracionNumerica(unittest.TestCase):

    def test_integracion(self):
        # Definir los parámetros de la prueba
        x = sp.symbols('x')
        func = x * (x**2 + 1)**(1/2)  # Función a integrar
        # Prueba con el método de Riemann
        resultado, error = integracion_riemann(func, 0, 1, 1000)
        self.assertAlmostEqual(error, 0, delta=0.01, msg="Error relativo en Riemann es demasiado alto")
        # Prueba con el método del Trapecio
        resultadoTrapecio, errorT = integracion_trapecio(func, 0, 1, 1000)
        self.assertAlmostEqual(errorT, 0, delta=0.01, msg="Error relativo en Trapecio es demasiado alto")

# Función de prueba
def test_func(x):
    return math.log(x) + x**2 - 4

class TestBiseccion(unittest.TestCase):

    def test_biseccion_raiz(self):
        """
        Test para verificar si la bisección encuentra correctamente la raíz.
        """
        raiz_encontrada, error_final = biseccion(test_func, 1, 2, 0.01)
        # Verificar si la raíz encontrada satisface la condición f(raiz) ≈ 0
        self.assertAlmostEqual(test_func(raiz_encontrada), 0, delta=0.055, msg="La raíz encontrada no es precisa.")

    def test_biseccion_error(self):
        """
        Test para verificar si el error es menor que la tolerancia especificada.
        """
        # Este test asume que biseccion() retorna tanto la raíz encontrada como el error final
        raiz_encontrada, error_final = biseccion(test_func, 1, 2, 0.01)
        self.assertLessEqual(error_final, 0.01, "El error final es mayor que la tolerancia especificada.")

# Si el script se ejecuta directamente, corre las pruebas
if __name__ == '__main__':
    unittest.main()
