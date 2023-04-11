import unittest
from ContadorPalabra import ContadorDePalabra

class TestContadorDePalabras(unittest.TestCase):

   def test_1 (self):

       resultado = ContadorDePalabra("hola como como")
       self.assertEqual(resultado,{
           'hola':1,
           'como':2
       })


if __name__ == '__main__':
    unittest.main()
