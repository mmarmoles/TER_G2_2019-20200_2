def Cesar:

    texto = input("Mensaje > ")

    n = int(input("Desplazamiento > "))

    abc = "abcdefghijklmnñopqrstuvwxyz"

    cifrado = ""

    for l in texto:
        if l in abc:
            pos_letra = abc.index(l)
            nueva_pos = (pos_letra + n) % len(abc)
            cifrado+= abc[nueva_pos]
        else:
            cifrado+= l

    print("Mensaje cifrado:", cifrado)

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