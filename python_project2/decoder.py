from cryptography.fernet import Fernet

encFile = input("Enter filename: ")

keyFile = input("Enter key file: ")

with open(encFile, "rb") as eFile:
    content = eFile.read()

with open(keyFile, "rb") as kFile:
    key = kFile.read() 

k = Fernet(key)

decFile = k.decrypt(content)

with open(encFile, "wb") as eFile:
    eFile.write(decFile)
    
print("The File has been successfully Decrypted!")
