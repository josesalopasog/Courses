import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra = 'Buen día'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DÍA') #Los primeros dos argumentos de assertEqual son dos valores que se comparan para establecer si hay igualdad entre ellos.
        
if __name__ == '__main__':
    unittest.main()       

        
