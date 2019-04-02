import pyAesCrypt
# This uses AES256-CBC to decrypt files and binary streams. 
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
# encrypt
pyAesCrypt.encryptFile("plaintext.pdf", "encrypted.pdf", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("encrypted.pdf", "decrypted.pdf", password, bufferSize)