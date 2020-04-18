# LIBRERIAS
import sys
from cryptosteganography import CryptoSteganography

# CLASES
class Datos:
    proceso = 0
    rutaFinalDeArchivo = ""
    nombreDeArchivo = "test.txt"
    rutaConArchivo = ""
    
    clave = ""
    claveTemp = ""
    clavecita = ""

    mensajeCifrado = ""
    mensajeDescrifado = ""

    textoGuardado = ""
    textoCesar = ""
    textoVigenere = ""

    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    fin = False       
    cifrarODescifrar = True

# FUNCIONES
def pasarAMayusculas():
    dato.textoGuardado = dato.textoGuardado.upper()

def CoreInicial():
    if dato.proceso == 0 : ValidarRutaInicial()
    elif dato.proceso == 1 : FicheroEnDescargas()
    elif dato.proceso == 2 : FicheroEnOtraRuta()
    elif dato.proceso == 3 : LecturaDeFichero()
    elif dato.proceso == 4 : CoreEncriptacion()

def CoreEncriptacion():
    dato.clave = input("Dame la clave de cifado / descifrado.\n")
    #dato.clave = dato.clave.upper()
    print("Ok, tu clave es: " + dato.clave)
    accion = "F"
    accion = input("Quieres cifrar (C) o Descifrar (D).\n")
    if accion == "C" or accion == "c":
        dato.cifrarODescifrar = True
    elif accion == "D" or accion == "d":
        dato.cifrarODescifrar = False


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
    #else:
        archivo.close()
        pasarAMayusculas()
        input("El mensaje es: \n" + dato.textoGuardado)

    ### FUNCIONES DE LOS CIFRADOS ###
    # CIFRADOS
def CifradoEstenogradia():
    split_message = [dato.textoGuardado [i:i + len(dato.clave)] for i in range(0, len(dato.textoGuardado), len(dato.clave))]
    for each_split in split_message:
        i = 0
        for letra in each_split:
            numero = (letra_indice[letra] + letra_indice[dato.clave[i]]) % len(dato.abcdario)
            mensajeCifrado += indice_letra[numero]
            i+=1
    dato.mensajeCifrado = encriptado
    
def CifradoVigenere():
    dato.textoGuardado = dato.textoGuardado.upper()
    #dato.textoGuardado = dato.textoGuardado.replace(' ', '').upper()
    dato.clave = dato.clave.replace(' ', '').upper()
    if len(dato.textoGuardado)>len(dato.clave):
        for i in range(int(len(dato.textoGuardado)/len(dato.clave))):
            dato.claveTemp += dato.clave
        dato.claveTemp += dato.clave[:len(dato.textoGuardado)%len(dato.clave)]	## longitud sea la misma que la del mensaje  ##
    elif len(dato.textoGuardado)<len(dato.clave):	# Si la longitud del mensaje es menor que la de la clave...
        dato.claveTemp = dato.clave[:len(dato.textoGuardado)]	# Se trunca la clave para que tenga la misma longitud que el mensaje #
    elif len(dato.textoGuardado)==len(dato.clave):	# Si la longitud del mensaje es igual que la de la clave... #
        dato.claveTemp = dato.clave	# Se guarda la clave tal cual se encuentra en 'clave_original' #
    else:
        print ('Ha ocurrido un error inesperado. Terminando ejecución...')
        sys.exit(1)
    print ('Mensaje original: ' + dato.textoGuardado)
    print ('Palabra clave: ' + dato.clave)
    print ()

    print ('Cifrando...')
    for i in range(len(dato.textoGuardado)):
        if dato.textoGuardado[i] == " ":
            i += 1
            dato.textoVigenere += " "
        else:
            x = dato.abc.find(dato.textoGuardado[i])	# Se guarda la posición del caracter del mensaje en el abecedario
            y = dato.abc.find(dato.claveTemp[i])	# Se guarda la posición del caracter de la clave en el abecedario
            suma = x+y	# Se calcula la suma de ambas posiciones
            modulo = suma%len(dato.abc)	# Se calcula el módulo de la suma respecto a la longitud del abecedario
            dato.textoVigenere += dato.abc[modulo]	# Se concatena el caracter cifrado con 'cifrado'
    print ('Mensaje cifrado: ' + dato.textoVigenere)
    print ()

def CifradoCesar():
    n = int(input("Desplazamiento > "))
    for l in dato.textoGuardado:
        if l in dato.abc:
            pos_letra = dato.abc.index(l)
            nueva_pos = (pos_letra + n) % len(dato.abc)
            dato.textoCesar += dato.abc[nueva_pos]
        else:
            dato.textoCesar += l        
    print("Mensaje Cesar:", dato.textoCesar, "\n")

def DescifradoEstenogradia():
    split_cipher = [dato.mensajeCifrado [i:i + len (dato.clave)] for i in range(0, len(cipher), len(dato.clave))]
    for each_split in split_cipher:
        i = 0
        for letra in each_split:
            numero = (letra_indice[letra] - letra_indice[dato.clave[i]]) % len(dato.abcdario)
            desencriptado += indice_letra[numero]
            i+=1
    dato.textoCesar = desencriptado
    crypto_steganography = CryptoSteganography('key')

    # Save the encrypted file inside the image | la imagen debe de estar en el mismo sito que está el código
    crypto_steganography.hide('image.png', 'output.png', 'encrypted_message') #no me funciona la llamda al mensaje encriptado.
    secret = crypto_steganography.retrieve('output.png')

def DescifradoVigenere():
    dato.textoGuardado = dato.textoGuardado.upper()
    #dato.textoGuardado = dato.textoGuardado.replace(' ', '').upper()
    dato.clave = dato.clave.replace(' ', '').upper()
    if len(dato.textoGuardado)>len(dato.clave):
        for i in range(int(len(dato.textoGuardado)/len(dato.clave))):
            dato.claveTemp += dato.clave
        dato.claveTemp += dato.clave[:len(dato.textoGuardado)%len(dato.clave)]	## longitud sea la misma que la del mensaje  ##
    elif len(dato.textoGuardado)<len(dato.clave):	# Si la longitud del mensaje es menor que la de la clave...
        dato.claveTemp = dato.clave[:len(dato.textoGuardado)]	# Se trunca la clave para que tenga la misma longitud que el mensaje #
    elif len(dato.textoGuardado)==len(dato.clave):	# Si la longitud del mensaje es igual que la de la clave... #
        dato.claveTemp = dato.clave	# Se guarda la clave tal cual se encuentra en 'clave_original' #
    else:
        print ('Ha ocurrido un error inesperado. Terminando ejecución...')
        sys.exit(1)
    print ('Mensaje original: ' + dato.textoGuardado)
    print ('Palabra clave: ' + dato.clave)
    print ()

    print ('Descifrando...')
    for i in range(len(dato.textoGuardado)):
        if dato.textoGuardado[i] == " ":
            i += 1
            dato.textoVigenere += " "
        else:
            x = dato.abc.find(dato.textoGuardado[i])	# Se guarda la posición del caracter del mensaje cifrado en el abecedario
            y = dato.abc.find(dato.claveTemp[i])	# Se guarda la posición del caracter de la clave en el abecedario
            resta = x-y	# Se calcula la resta de ambas posiciones
            modulo = resta%len(dato.abc)	# Se calcula el módulo de la resta respecto a la longitud del abecedario
            dato.textoVigenere += dato.abc[modulo]	# Se concatena el caracter descifrado con 'descifrado'
    print ('Mensaje descifrado: ' + dato.textoVigenere)
    print ()

def DescifradoCesar():
    i = int(input("Desplazamiento > "))
    for l in dato.textoGuardado:
        if l in dato.abc:
            pos_letra = dato.abc.index(l)
            nueva_pos = (pos_letra - i) % len(dato.abc)
            dato.textoCesar += dato.abc[nueva_pos]
        else:
            dato.textoCesar += l
    print("Mensaje:", dato.textoCesar, "\n")

# PROGRAMA
dato = Datos()
clave = ""
while dato.fin != True:
    CoreInicial()
print(dato.textoGuardado)