from cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography('uoc')

# Save the encrypted file inside the image
crypto_steganography.hide('chamelon.jpg', 'output.png', 'A ver cuantos caracteres aguanta y si realmente puede ser tan útil como parece... veremos si lo agunta a o no')

secret = crypto_steganography.retrieve('output.png')

print(secret)
# My secret message
