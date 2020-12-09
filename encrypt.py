from Crypto import Random
from Crypto.Cipher import AES
from pyDes import *


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")


def encryptAESfile(key):
    file_name = input("Please enter the path to the file to be encrypted: ")
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)

def decryptAESfile(key):
    file_name = input("Please enter the path to the file to be decrypted: ")
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)


def encryptDESFile(k):

    file_name = input("Please enter the path to the file to be encrypted: ")
    f = open(file_name, "rb+")
    d = f.read()
    f.close()
 
    d = k.encrypt(d, " ")
    f = open(file_name + ".enc", "wb+")
    f.write(d)
    f.close()

def decryptDESFile(k):

    file_name = input("Please enter the path to the file to be decrypted: ")
    f = open(file_name, "rb+")
    d = f.read()
    d = k.decrypt(d, " ")
    f = open(file_name[:-4], "wb+")
    f.write(d)
    f.close()


keyAES = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
keyDES = des("MyDESkey")

a = int(input(":: Welcome to Encryption/Decryption ::\n"

                    "1. AES\n2. DES\n3. Back\n"))

if (a == 1):

    b = int(input(":: Welcome to AES Encryption ::\n"

						"1. Encrypt\n2. Decrypt\n3. Back\n"))

    if (b == 1):

        encryptAESfile(keyAES)

    elif (b == 2):

        decryptAESfile(keyAES)
		
    elif(b==3):

        exec(open("./encrypt.py").read())

    else:

        raise Exception("Enter correct input")

elif (a == 2):

    c = int(input(":: Welcome to DES Encryption ::\n"

						"1. Encrypt\n2. Decrypt\n3. Back\n"))

    if (c == 1):

        encryptDESFile(keyDES)

    elif (c == 2):

        decryptDESFile(keyDES)
		
    elif(c==3):

        exec(open("./encrypt.py").read())

    else:

        raise Exception("Enter correct input")
    
elif(a==3):

    exec(open("./CyberScript.py").read())

else:

    raise Exception("Enter correct input")
