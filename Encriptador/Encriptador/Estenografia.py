from cryptosteganography import CryptoSteganography

print("Entrar la contraseña a usar: \n")
key = input ()
print(key)

print("Entrar el mensaje secreto: \n")
message = input ()
print(message)

crypto_steganography = CryptoSteganography(key)

# Save the encrypted file inside the image
crypto_steganography.hide('chamelon.jpg', 'output.png', message)





secret = crypto_steganography.retrieve('output.png')

