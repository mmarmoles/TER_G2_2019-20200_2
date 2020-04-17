#!/usr/bin/env python
#-*- coding: utf-8 -*-

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
            if j < len(key):
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


dato = Datos()
def main():
  #  while dato.fin != True:
   #     CoreInicial()
    #print(dato.textoGuardado)


    print("El mensaje y la clave solo pueden estar en alfabetico")
    choice = int(input("1. Comprimir\n2. Descomprimir\nElige(1,2): "))
    if choice == 1:
        while dato.fin != True:
            CoreInicial()
        print(dato.textoGuardado)

        print("Encriptando")
        message, mapped_key = msg_and_key()
        cipher_encryption(message, mapped_key)

    elif choice == 2:
        while dato.fin != True:
            CoreInicial()
        print(dato.textoGuardado)

        print("Desencriptando")
        message, mapped_key = msg_and_key()
        cipher_decryption(message, mapped_key)

    else:
        print("Error, tienes que escribir 1 o 2")

    
if __name__ == "__main__":
    main()