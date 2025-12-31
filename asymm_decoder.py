# asymm_decoder.py
import rsa

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
    
encFile = input("Enter the filename or path of the encoded file: ")

with open(encFile, "rb") as f:
    eFile = f.read()
    
decFile = rsa.decrypt(eFile, private_key)

with open(encFile, "wb") as f:
    f.write(decFile)

print("File decrypted successfully!")
