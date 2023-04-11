import unittest

def ContadorDePalabra(frase):
    result = {}
    lista = frase.split(' ')
    for clave in lista:
        if clave in result:
            result[clave] += 1
        else:
            result[clave] = 1
    return result

if __name__ == '__main__':
    unittest.main()
