from cryptography.fernet import Fernet

key = Fernet.generate_key()
k = Fernet(key)

filename = input("Enter filename or filepath: ")

with open(filename, "rb") as file:
    content = file.read()

encryptedContent = k.encrypt(content)

with open(filename, "wb") as file:
    file.write(encryptedContent)
    print("File encrypted successfully")

with open("fileKey.txt", "wb") as keyFile:
    keyFile.write(key)
    
print(f"Public Key for {filename} written to keyFile.txt")
