import unittest
import sympy as sp
from newtonConTest import newton_raphson_sympy

class TestNewtonRaphson(unittest.TestCase):
    def test_root_finding(self):
        x = sp.symbols('x')
        # Ejemplo de función: x^2 - 4, cuya raíz sabemos que es ±2.
        func = sp.log(x)+x**2-4
        # Prueba con una aproximación inicial cerca de la raíz positiva
        root = newton_raphson_sympy(func, x0=1.5, tol=0.01)
        self.assertAlmostEqual(root, 1.8410, places=2, msg="La raíz encontrada no es precisa.")

    def test_convergence_failure(self):
        x = sp.symbols('x')
        # Ejemplo de función con derivada que puede ser cero: x^3 - 2*x + 2
        func = x**2
        # Prueba con una aproximación inicial que puede no converger fácilmente
        root = newton_raphson_sympy(func, x0=1.5, tol=0.01, max_iter=100)
        # Aquí, puedes decidir cómo manejar un caso de convergencia fallida. Si tu función
        # retorna None o lanza una excepción en caso de falla, asegúrate de manejarlo aquí.
        # Este ejemplo simplemente verifica si la función termina sin encontrar una raíz, 
        # pero es posible que necesites ajustar esta prueba según el comportamiento exacto de tu función.
        self.assertIsNone(root, "La función debería indicar una falla en la convergencia.")

# Si el script se ejecuta directamente, corre las pruebas
if __name__ == '__main__':
    unittest.main()
