# LIBRERIAS
from cryptosteganography import CryptoSteganography

# CLASES
class Datos:
    proceso = 0
    rutaFinalDeArchivo = ""
    nombreDeArchivo = "test.txt"
    rutaConArchivo = ""
    textoGuardado = ""
    clave = ""
    mensajeCifrado = ""
    mensajeDescrifado = ""

    textoCesar = ""

    fin = False       
    cifrarODescifrar = True

# FUNCIONES
def CoreInicial():
    if dato.proceso == 0 : ValidarRutaInicial()
    elif dato.proceso == 1 : FicheroEnDescargas()
    elif dato.proceso == 2 : FicheroEnOtraRuta()
    elif dato.proceso == 3 : LecturaDeFichero()
    elif dato.proceso == 4 : CoreEncriptacion()

def CoreEncriptacion():
    dato.clave = input("Dame la clave de cifado / descifrado.\n")
    print("Ok, tu clave es: " + dato.clave)
    accion = "F"
    if accion == "C" or accion == "c":
        dato.cifrarODescifrar = True
    elif accion == "D" or accion == "d":
        dato.cifrarODescifrar = False
    else:
        accion = input("Quieres cifrar (C) o Descifrar (D).\n")

    if dato.cifrarODescifrar == True:
        print("Cifrando...")
        #CifradoEstenogradia()
        #CifradoVigenere()
        CifradoCesar()
        #CifradoPalabraClave()
    else: 
        print("Descifrando...")
        #DescifradoPalabraClave()
        DescifradoCesar()
        #DescifradoVigenere()
        #DescifradoEstenogradia()

def msg_and_key():
    msg = dato.textoGuardado.upper()
    #msg = input("Enter message: ").upper()
    key = input("Enter key: ").upper()
    #variable to store mapped key
    key_map = ""

    j = 0
    for i in range(len(msg)):
        if ord(msg[i]) == 32:
        #ignoring space
            key_map += " "
        else:
            if j < len(dato.clave):
                key_map += key[j]
                j += 1
            else:
                j = 0
                key_map += key[j]
                j += 1

    return msg, key_map

def create_vigenere_table():
    table = []
    for i in range(26):
        table.append([])

    for row in range(26):
        for column in range(26):
            if (row + 65) + column > 90:
              #moving back to A after Z
                table[row].append(chr((row+65) + column - 26))
            else:
                table[row].append(chr((row+65) + column))

    return table

def cipher_encryption(message, mapped_key):
    table = create_vigenere_table()
    encrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            encrypted_text += " "
        else:
            #getting element at specific index of table
            row = ord(message[i]) - 65
            column = ord(mapped_key[i]) - 65
            encrypted_text += table[row][column]

    print("Mensaje Encriptado: {}".format(encrypted_text))

def itr_count(mapped_key, message):
    counter = 0
    result = ""

    #starting alphabets from mapped key letter and finishing all 26 letters from it(form z move to a)
    for i in range(26):
        if mapped_key + i > 90:
            result += chr(mapped_key + (i-26))
        else:
            result += chr(mapped_key + i)

    #counting the number of iterations it take from mapped key to ciphertext letter
    for i in range(len(result)):
        if result[i] == chr(message):
            break
        else:
            counter += 1        
    return counter

def cipher_decryption(message, mapped_key):
    table = create_vigenere_table()
    decrypted_text = ""

    for i in range(len(message)):
        if message[i] == chr(32):
            # ignoring space
            decrypted_text += " "
        else:
            # adding number of iterations, it takes to reach from mapped key letter to cipher letter in 65
            # by doing so we get column header of ciphertext letter, which happens to be decrypted letter
            decrypted_text += chr(65 + itr_count(ord(mapped_key[i]), ord(message[i])))

    print("Decrypted Message: {}".format(decrypted_text))

def ValidarRutaInicial():
    print("Bienvenido al Engriptador. \n")
    preguntaInicial = input("Por favor indicanos si el archivo se encuentra en DESCARGAS (S/N) \n")        
    if preguntaInicial == "S" or preguntaInicial == "s":
        archivoEnDescargas = True
        print("De acuerdo el archivo se encuentra en DESCARGAS \n")
        dato.proceso = 1
    elif preguntaInicial == "N" or preguntaInicial == "n":
        archivoEnDescargas = False
        print("De acuerdo el archivo no se encuentra en DESCARGAS (Buscaré en la carpeta del ejecutable) \n")
        dato.proceso = 2

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
    rutaFinalDeArchivo = "test.txt"
    print("La ruta de tu archivo es: " + rutaFinalDeArchivo)
    dato.proceso = 3
    dato.rutaFinalDeArchivo = rutaFinalDeArchivo

def LecturaDeFichero():
    dato.rutaConArchivo = dato.rutaFinalDeArchivo + "/" + dato.nombreDeArchivo
    if dato.textoGuardado == "":
        archivo = open(dato.rutaConArchivo, 'r')
        dato.textoGuardado = archivo.read()
        dato.proceso = 4
    else:
        archivo.close()
        input("El mensaje es: \n" + dato.textoGuardado)
    

### FUNCIONES DE LOS CIFRADOS ###
    # CIFRADOS
def CifradoEstenogradia():
    split_message = [dato.textoGuardado [i:i + len(dato.clave)] for i in range(0, len(dato.textoGuardado), len(dato.clave))]
    for each_split in split_message:
        i = 0
        for letra in each_split:
            numero = (letra_indice[letra] + letra_indice[dato.clave[i]]) % len(abcdario)
            mensajeCifrado += indice_letra[numero]
            i+=1
    dato.mensajeCifrado = encriptado
    
#def CifradoVigenere():

def CifradoCesar():
    n = int(input("Desplazamiento > "))
    abc = "abcdefghijklmnñopqrstuvwxyz"
    for l in dato.textoCesar:
        if l in abc:
            pos_letra = abc.index(l)
            nueva_pos = (pos_letra + n) % len(abc)
            dato.mensajeCifrado += abc[nueva_pos]
        else:
            cifrado+= l
def DescifradoEstenogradia():
    split_cipher = [dato.mensajeCifrado [i:i + len (dato.clave)] for i in range(0, len(cipher), len(dato.clave))]
    for each_split in split_cipher:
        i = 0
        for letra in each_split:
            numero = (letra_indice[letra] - letra_indice[dato.clave[i]]) % len(abcdario)
            desencriptado += indice_letra[numero]
            i+=1
    dato.mensajeDescrifado = desencriptado
    crypto_steganography = CryptoSteganography('key')

    # Save the encrypted file inside the image | la imagen debe de estar en el mismo sito que está el código
    crypto_steganography.hide('image.png', 'output.png', 'encrypted_message') #no me funciona la llamda al mensaje encriptado.
    secret = crypto_steganography.retrieve('output.png')
def DescifradoCesar():
    for i in range(28):
        descifrado = ""
        for l in texto:
            if l in abc:
                pos_letra = abc.index(l)
                nueva_pos = (pos_letra - i) % len(abc)
                descifrado += abc[nueva_pos]
            else:
                descifrado+= l
        msj = (descifrado)
    print("Mensaje:", msj)

# VARIABLES STATICAS
abcdario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ 0987654321.:;()/\_-!#"<>¿?@abcdefghijklmnñopqrstuvwxyz'
letra_indice = dict(zip(abcdario, range(len(abcdario))))
indice_letra = dict(zip(range(len(abcdario)), abcdario))

# PROGRAMA
dato = Datos()
while dato.fin != True:
    CoreInicial()
print(dato.textoGuardado)