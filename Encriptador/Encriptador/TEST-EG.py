# CLASES
class Datos:
    proceso = 0
    rutaFinalDeArchivo = ""
    nombreDeArchivo = "test.txt"
    rutaConArchivo = ""
    textoGuardado = ()
    fin = False

# FUNCIONES
def CoreInicial():
    if dato.proceso == 0 : ValidarRutaInicial()
    elif dato.proceso == 1 : FicheroEnDescargas()
    elif dato.proceso == 2 : FicheroEnOtraRuta()
    elif dato.proceso == 3 : LecturaDeFichero()

def ValidarRutaInicial():
    print("Bienvenido al Encriptador. \n")
    preguntaInicial = "Ç"
    preguntaInicial = input("Por favor indicanos si el archivo se encuentra en DESCARGAS (S/N) \n")
    if preguntaInicial == "S" or preguntaInicial == "s":
        archivoEnDescargas = True
        print("De acuerdo el archivo se encuentra en DESCARGAS \n")
        dato.proceso = 1
    elif preguntaInicial == "N" or preguntaInicial == "n":
        archivoEnDescargas = False
        print("De acuerdo el archivo no se encuentra en DESCARGAS \n")
        dato.proceso = 2
    else:
        preguntaInicial = input("Por favor indicanos si el archivo se encuentra en DESCARGAS (S/N) \n")
        
def FicheroEnDescargas():
    print("Vale ahora necesitare tu nombre de usuario de WINDOWS. \n")
    usuarioLocalWindows = input("Si no lo sabes, ejecuta esta linea en el CMD y mira haver cual te cuadra: wmic useraccount get name,fullname\n")
    rutaFinalDeArchivo = "C:/Users/"
    rutaFinalDeArchivo += usuarioLocalWindows
    rutaFinalDeArchivo += "/Downloads"
    print("La ruta de tu escritorio es: " + rutaFinalDeArchivo)
    dato.proceso = 3
    dato.rutaFinalDeArchivo = rutaFinalDeArchivo

def FicheroEnOtraRuta():
    rutaFinalDeArchivo = input("vale, dame la ruta ABSOLUTA o RELATIVA (donde está el archivo .txt), donde esté el fichero a tratar\n")
    print("La ruta de tu archivo es: " + rutaFinalDeArchivo)
    dato.proceso = 3
    dato.rutaFinalDeArchivo = rutaFinalDeArchivo

def LecturaDeFichero():
    dato.rutaConArchivo = dato.rutaFinalDeArchivo + "/" + dato.nombreDeArchivo
    archivo = open(dato.rutaConArchivo, 'r')
    dato.textoGuardado = archivo.read()
    archivo.close()
    dato.fin = True

# PROGRAMA - COMPROBACIÓN DE QUE LOS DATOS INTRODUCIDOS SON CORRECTOS
dato = Datos()
while dato.fin != True:
    CoreInicial()
print('Mensaje original en txt: ' + dato.textoGuardado)

# ENCRIPTACIÓN DEL TEXTO

# VARIABLES
abcdario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ 0987654321.:;()/\_-!#"<>¿?@abcdefghijklmnñopqrstuvwxyz'
letra_indice = dict(zip(abcdario, range(len(abcdario))))
indice_letra = dict(zip(range(len(abcdario)), abcdario))

# FUNCION DE ENCRYPTACION
def encrypt(message, key):
    encrypted = ''
    split_message = [message [i:i + len (key)] for i in range(0, len(message), len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letra_indice[letter] + letra_indice[key[i]]) % len(abcdario)
            encrypted += indice_letra[number]
            i+=1

    return encrypted


# FUNCION DE ENCRYPTACION
def dencrypt(cipher, key):
    decrypted = ''
    split_cipher = [cipher [i:i + len (key)] for i in range(0, len(cipher), len(key))]
    for each_split in split_cipher:
        i = 0
        for letter in each_split:
            number = (letra_indice[letter] - letra_indice[key[i]]) % len(abcdario)
            decrypted += indice_letra[number]
            i+=1

    return decrypted

def main():
    key = 'hola'
    message = dato.textoGuardado
    encrypted_message = encrypt(message, key)
    dencrypted_message = dencrypt(encrypted_message, key)

    print('Mensaje original: ' + message)
    print('Mensaje encyptado: ' + encrypted_message)
    print('Mensaje desencryptado: ' + dencrypted_message)
    print('La clave usada: ' + key)

main()

# LLAMADA A LAS FUNCIONES NECESARIAS PARA LA ESTENOGRAFIA

from cryptosteganography import CryptoSteganography

# print("Entrar la contraseña a usar: \n")
# key = input ()
#print(key)

# print("Entrar el mensaje secreto: \n")
# message = input ()
# print(message)

crypto_steganography = CryptoSteganography('key')

# Save the encrypted file inside the image | la imagen debe de estar en el mismo sito que está el código
crypto_steganography.hide('chamelon.jpg', 'output.png', 'encrypted_message') #no me funciona la llamda al mensaje encriptado.
secret = crypto_steganography.retrieve('output.png')

# My secret message
print(secret)

