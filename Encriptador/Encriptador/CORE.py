# VARIABLES 

proceso = 0

# FUNCIONES
def validarBoolRutaInicial(proceso):
    preguntaInicial = "F"
    while proceso != 1:
        if preguntaInicial == "S" or preguntaInicial == "s":
                archivoEnDescargas = True
                print("De acuerdo el archivo se encuentra en DESCARGAS \n")
                proceso = 1
        elif preguntaInicial == "N" or preguntaInicial == "n":
              archivoEnDescargas = False
              print("De acuerdo el archivo no se encuentra en DESCARGAS \n")
              proceso = 1
        else:
            preguntaInicial = input("Por favor indicanos si el archivo se encuentra en DESCARGAS (S/N) \n")

# PROGRAMA

print("Bienvenido al Engriptador \n")
validarBoolRutaInicial(proceso);