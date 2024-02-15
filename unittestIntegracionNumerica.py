import unittest
import sympy as sp
from integracionConTest import integracion_numerica, evaluar_funcion

class TestIntegracionNumerica(unittest.TestCase):

    def test_integracion_numerica(self):
        x = sp.symbols('x')
        func = x * (x**2 + 1)**(1/2)  # Función para el test
        a = 0  # Límite inferior
        b = 1  # Límite superior
        n = 1000  # Número de subintervalos para una mejor precisión
        
        # Calcula la aproximación numérica
        resultado = integracion_numerica(func, a, b, n)
        
        # Calcula el valor real de la integral
        integral_exacta = sp.integrate(func, (x, a, b))
        valor_real = float(integral_exacta.evalf())
        
        # Calcula el error relativo
        error = abs((valor_real - resultado) / valor_real)
        
        # Afirmación: el error relativo debe ser menor que un umbral específico
        self.assertTrue(error < 0.01, "El error relativo es demasiado grande.")

if __name__ == '__main__':
    unittest.main()
