import unittest
import sympy as sp
from integracionConTest import integracion_riemann, integracion_trapecio

# Las funciones de integración se mantienen igual a las definidas anteriormente

# Integración por Riemann y Trapecio definidas previamente aquí

class TestIntegracionNumerica(unittest.TestCase):

    def test_integracion(self):
        # Definir los parámetros de la prueba
        x = sp.symbols('x')
        func = x * (x**2 + 1)**(1/2)  # Función a integrar
        # Prueba con el método de Riemann
        resultado, error = integracion_riemann(func, 0, 1, 4)
        self.assertAlmostEqual(error, 0, delta=0.4, msg="Error relativo en Riemann es demasiado alto")
        # Prueba con el método del Trapecio
        resultadoTrapecio, errorT = integracion_trapecio(func, 0, 1, 4)
        self.assertAlmostEqual(errorT, 0, delta=0.4, msg="Error relativo en Trapecio es demasiado alto")

if __name__ == '__main__':
    unittest.main()
