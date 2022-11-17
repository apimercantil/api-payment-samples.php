"""Este modulo implementa una clase para el cifrado AES 128-cbc, utilizado por la API
de Mercantil Banco para la transmisi'on de datos sensibles.

Toma como base la clase para PHP definida en el archivo `AesCipher.php` del repositorio
p'ublico de Mercantil Banco.

LICENCIA MIT: 
=============================
   Se puede copiar, redistribuir y/o modificar el c'odigo libremente, pero
   manteniendo la referencia a la fuente original.

README:
==============================================
1. Esta version utiliza el modulo Crypto, instalado con el paquete PyCryptodome
   (https://pycryptodome.readthedocs.io/en/latest/src/introduction.html), que es
   el reemplazo de PyCrypto (obsoleto).

   Para instalarlo, con pip:

   python -m pip install PyCryptodome

   o:

   python3 -m pip install PyCryptodome

   Para m'as informaci'on, consultar
   https://pycryptodome.readthedocs.io/en/latest/src/installation.html

2. Ejemplos:
   - https://stackoverflow.com/questions/66862391/aes-128-cbc-encryption-in-python
   - https://stackoverflow.com/questions/46904355/aes-128-cbc-decryption-in-python
   - https://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes/14205319
"""

import os, sys
from sys import argv, exit, stdin, stdout, stderr

from base64 import b64encode, b64decode
from Crypto.Hash import SHA256     # para generar el hash de `sha256`
from Crypto.Cipher import AES      # cifrado/descifrado AES 256 CBC
from Crypto.Util.Padding import pad, unpad

__author__    = "Yoel Monsalve | yoel@vditech.us"
__date__      = "2022-11-16"
__modified__  = "2022-11-17"
__version__   = ""


class AesCipher:

	# Miembros "pseudo-estaticos", o constantes
	# 
	# NOTA: Aunque no existe tal cosa como miembros "est'aticos" de clase
	# en Python (https://stackoverflow.com/questions/3506150/static-class-members-python),
	# estos pueden ser simulados mediante miembros con 'ambito de clase, definidos
	# junto con la misma, que son cargados en tiempo de importaci'on.
	# 
	# Se pueden referenciar sin necesidad de crear instancias de la clase.
	OPENSSL_CIPHER_MODE = AES.MODE_ECB
	CIPHER_KEY_LEN = 16

	def __init__(self):
		return

	def createKeyHash(keybank=''):
		"""Obtiene el hash de una via 256, a partir de la clave secreta
		dada por el banco.

		- Codificar cadena en UTF-8:
		    - https://www.geeksforgeeks.org/python-convert-string-to-bytes/
			- https://docs.python.org/3/howto/unicode.html
		- SHA256 en Python:
		    - https://docs.python.org/3/library/hashlib.html
		
		Args:
			keybank (str): clave secreta (como cadena) (default: `''`)

		Returns:
			bytes: SHA256 de la clave secreta
		"""
		if not keybank: return None

		keybank_bytes = keybank.encode('utf-8')

		return SHA256.new(keybank_bytes).digest()

	def fixKey(key):
		"""Selecciona los primeros 16 bytes del hash de la clave
		enviada por el banco.
		
		Args:
			key (bytes): hash de la clave
		
		Returns:
			bytes: primeros 16 bytes del hash de la clave
		"""
		if len(key) < AesCipher.CIPHER_KEY_LEN:
			# completar los primeros 16 bytes con cero
			key += bytes(AesCipher.CIPHER_KEY_LEN - len(key))
		elif len(key) > AesCipher.CIPHER_KEY_LEN:
			# trunca a los primeros 16 bytes
			key = key[:AesCipher.CIPHER_KEY_LEN]
		
		return key

	def encrypt(key=b'\0', data=''):
		"""Encripta mensaje en AES ECB 128 bits
		
		Args:
			key (bytes): hash SHA256 de la clave enviada por el banco. Debe 
			              truncar el hash a 16 bytes de longitud.
			data (str): dato a ser cifrado.

		Returns:
            bytes: base64-encoded del mensaje cifrado
		"""

		# ajustar la clave a 16 bytes
		key = AesCipher.fixKey(key)
		# objeto encriptador
		cipher = AES.new(key, AES.MODE_ECB)
		# rellenar el mensaje, para alinear con el tama~no de bloque
		msg = pad(data.encode('utf-8'), AES.block_size)
		# mensaje cifrado
		msg_encrypted = cipher.encrypt(msg)
		
		return b64encode(msg_encrypted)

	def decrypt(key=b'\0', data_enc=''):
		"""Desencripta el mensaje previamente cifrado en AES ECB 128 bits
		
		Args:
			key (bytes): hash SHA256 de la clave enviada por el banco. Debe 
			              truncar el hash a 16 bytes de longitud.
			data_enc (bytes): data cifrada, y encodificada base64

		Returns:
            str: data descifrada, en texto plano
		"""

		# ajustar la clave a 16 bytes
		key = AesCipher.fixKey(key)
		# objeto encriptador
		cipher = AES.new(key, AES.MODE_ECB)
		# mensaje descifrado
		msg = cipher.decrypt(b64decode(data_enc))
		# des-rellenar el mensaje, para alinear con el tama~no de bloque
		msg = unpad(msg, AES.block_size)
		# y pasar de bytes a str
		msg = msg.decode('utf-8')
		
		return msg
