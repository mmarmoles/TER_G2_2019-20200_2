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

    pass

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
    key = 'cualquiercosa1983'
    message = 'Este es un mensaje para el 620791859 con info personal gutiylla@gmail.com '
    encrypted_message = encrypt(message, key)
    dencrypted_message = dencrypt(encrypted_message, key)

    print('Mensaje original: ' + message)
    print('Mensaje encyptado: ' + encrypted_message)
    print('Mensaje desencryptado: ' + dencrypted_message)
    print('La clave usada: ' + key)

main()