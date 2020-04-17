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
    print("Bienvenido al Engriptador. \n")
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

# PROGRAMA
dato = Datos()
while dato.fin != True:
    CoreInicial()
print(dato.textoGuardado)