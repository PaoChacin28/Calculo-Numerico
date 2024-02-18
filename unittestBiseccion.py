import unittest
import math
from biseccionConTest import biseccion
# Aquí iría la definición de tu función biseccion()

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

if __name__ == "__main__":
    unittest.main()
