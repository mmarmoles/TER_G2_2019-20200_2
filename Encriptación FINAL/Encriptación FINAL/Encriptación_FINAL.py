# LIBRERIAS
from cryptosteganography import CryptoSteganography

# CLASES
class Datos:
    proceso = 0
    rutaFinalDeArchivo = ""
    nombreDeArchivo = "test.txt"
    rutaConArchivo = ""
    textoGuardado = ""
    fin = False       
    clave = ""
    mensajeCifrado = ""
    mensajeDescrifado = ""
    fin = False

# FUNCIONES
def CoreInicial():
    if dato.proceso == 0 : ValidarRutaInicial()
    elif dato.proceso == 1 : FicheroEnDescargas()
    elif dato.proceso == 2 : FicheroEnOtraRuta()
    elif dato.proceso == 3 : LecturaDeFichero()    
def CoreEncriptacion(CifrarODescifrar):
    if CifrarODescifrar == True:
        print("Descifrando...")
        CifradoEstenogradia()
        CifradoVigenere()
        CifradoCesar()
        CifradoPalabraClave()
    else: 
        print("Cifrando...")
        DescifradoPalabraClave()
        DescifradoCesar()
        DescifradoVigenere()
        DescifradoEstenogradia()

def ValidarRutaInicial():
    print("Bienvenido al Engriptador. \n")
    preguntaInicial = "Ç"
    preguntaInicial = input("Por favor indicanos si el archivo se encuentra en DESCARGAS (S/N) \n")
    if preguntaInicial == "S" or preguntaInicial == "s":
        archivoEnDescargas = True
        print("De acuerdo el archivo se encuentra en DESCARGAS \n")
        dato.clave = input("Dame la clave de cifado / descifrado.")
        print("Ok, tu clave es: " + dato.clave)
        dato.proceso = 1
    elif preguntaInicial == "N" or preguntaInicial == "n":
        archivoEnDescargas = False
        print("De acuerdo el archivo no se encuentra en DESCARGAS \n")
        dato.clave = input("Dame la clave de cifado / descifrado.")
        print("Ok, tu clave es: " + dato.clave)
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
    rutaFinalDeArchivo = input("vale, dame la ruta ABSOLUTA o RELATIVA (donde está el archivo .exe), donde esté el fichero a tratar.\n")
    print("La ruta de tu archivo es: " + rutaFinalDeArchivo)
    dato.proceso = 3
    dato.rutaFinalDeArchivo = rutaFinalDeArchivo
def LecturaDeFichero():
    dato.rutaConArchivo = dato.rutaFinalDeArchivo + "/" + dato.nombreDeArchivo
    archivo = open(dato.rutaConArchivo, 'r')
    dato.textoGuardado = archivo.read()
    archivo.close()
    dato.fin = True

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
    for l in texto:
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

### JUANJO - CESAR

##texto = input("Mensaje > ")

#n = int(input("Desplazamiento > "))

#abc = "abcdefghijklmnñopqrstuvwxyz"

##cifrado = ""

#for l in texto:
#    if l in abc:
#        pos_letra = abc.index(l)
#        nueva_pos = (pos_letra + n) % len(abc)
#        cifrado+= abc[nueva_pos]
#    else:
#        cifrado+= l

## print("Mensaje cifrado:", cifrado)

# DESCIFRADO
#for i in range(28):
#    descifrado = ""
 #   for l in texto:
  #      if l in abc:
   #         pos_letra = abc.index(l)
    #        nueva_pos = (pos_letra - i) % len(abc)
     #       descifrado += abc[nueva_pos]
      #  else:
       #     descifrado+= l
   # msj = (descifrado)
#print("Mensaje:", msj)

