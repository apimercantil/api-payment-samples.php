"""
Ejemplo de uso de la clase AesCipher.

Se toma un dato secreto, se encripta y se desencripta. Para verificar
que se devuelve el original.
"""
__author__    = "Yoel Monsalve | yoel@vditech.us"
__date__      = "2022-11-16"
__modified__  = "2022-11-17"
__version__   = ""

import sys
import os

# directorio donde esta ubicada la clase AesCipher
if not os.path.abspath( os.path.dirname( __file__ ) + "/..") in sys.path:
	sys.path.append( os.path.abspath( os.path.dirname( __file__ ) + "/.." ))
from AesCipher import AesCipher

print('''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	Ejemplo de uso de modulo API
	Cortesia de Mercantil Banco

	https://apiportal.mercantilbanco.com/mercantil-banco/produccion/
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')

print('Genera el CVV, el valor cifrado, y des-cifrado')

# Dato privado: CVV
cvv = '752'

# Clave secreta enviada por el Banco
keybank = 'A9279120481620090622AA30'

# Generacion del hash a partir de la clave secreta del Banco
keyhash = AesCipher.createKeyHash(keybank);

cvv_encrypted = AesCipher.encrypt(keyhash, cvv)
cvv_decrypted = AesCipher.decrypt(keyhash, cvv_encrypted)

print(f'CVV utilizado     : {cvv}')
print(f'CVV encryptado    : {cvv_encrypted}')
print(f'CVV des-encryptado: {cvv_decrypted}')