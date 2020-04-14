# VARIABLES
abcdario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letra_indice = dict(zip(abcdario, range(len(abcdario))))
inidce_letra = dict(zip(range(len(abcdario)), abcdario))

# FUNCION DE ENCRYPTACION
def encrypt(message, key):
    encrypted = ''
    split_message = [message [i:i + len (key)] for i in range(0, len(message), len(key))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letra_indice[letter] + letra_indice[key[i]]) % len(abcdario)
            encrypted += inidce_letra[number]
            i+=1

    return encrypted

    pass

 # FUNCION DE ENCRYPTACION
def dencrypt(message, key):





    pass


def main():
    key = 'MARC'
    message = 'ENCRIPTADO'
    encrypted_message = encrypt(message, key)
    print(encrypted_message)

    pass

main()