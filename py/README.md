# README:

## Requisitos

Esta versión utiliza el modulo Crypto, instalado con el paquete [`PyCryptodome`](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html), que es el reemplazo de PyCrypto (_obsoleto_).

Para instalar `Cryptodome`, con pip:

```
    python -m pip install PyCryptodome
```

o:

```
    python3 -m pip install PyCryptodome
```

Para más información, consultar la página [_instalación_](https://pycryptodome.readthedocs.io/en/latest/src/installation.html).

### Ejemplos de uso de `PyCryptodome`:

- https://stackoverflow.com/questions/66862391/aes-128-cbc-encryption-in-python
- https://stackoverflow.com/questions/46904355/aes-128-cbc-decryption-in-python
- https://stackoverflow.com/questions/14179784/python-encrypting-with-pycrypto-aes/14205319

## Descripción

La clase base para el cifrado de datos se encuentra en el archivo `AesCipher.py`, y se deriva del ejemplo proporcionado en PHP, pero versionado a Python. Se utilizan métodos pseudo "estáticos" (que se pueden invocar sin definir un objeto de la clase) para mantener el diseño original. Ejemplo:

```python
AesCipher.encrypt(mi_dato)
```

en lugar de:

```python
Cipher = AesCipher()        # objeto de la clase
Cipher.encrypt(mi_dato)     # llamar m'etodo del objeto
```

## Estructura de archivos

```
py
`+-- AesCypher.py        # clase base de cifrado
 |-- test
     `--- cipher.py      # script de prueba clase AesCypher 
```

## Uso del test

Se ha creado una carpeta `test`, con un código de prueba qu encripta y desencripta el mismo dato, para comprobar que devuelve el resultado original. Para probarlo, invocar desde la terminal de comandos:

```bash
python py/test/cipher.py
```
o
```bash
py py/test/cipher.py
```

Salida:
```

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   Ejemplo de uso de modulo API
   Cortesia de Mercantil Banco

   https://apiportal.mercantilbanco.com/mercantil-banco/produccion/
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Genera el CVV, el valor cifrado, y des-cifrado
CVV utilizado     : 752
CVV encryptado    : b'BCqzVtesja27ClW0fi4EfA=='
CVV des-encryptado: 752
```
que es la misma que en el script de PHP.