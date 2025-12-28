import rsa
import os

# 1. Increased key size to 2048 to allow larger files
# 2. Logic to SAVE/LOAD keys so they don't change every time you run the script
if not os.path.exists("private.pem"):
    print("Generating and saving new keys...")
    publicKey, privateKey = rsa.newkeys(2048) 
    with open("private.pem", "wb") as f:
        f.write(privateKey.save_pkcs1())
    with open("public.pem", "wb") as f:
        f.write(publicKey.save_pkcs1())
else:
    with open("private.pem", "rb") as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())
    with open("public.pem", "rb") as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())

choice1 = input("Encrypt (e) or Dycrypt (d): ")

match choice1:
    case "e":
        encFilename = input("Enter the filename of the file To encrypt: ")

        with open(encFilename, "rb") as file0:
            content = file0.read()
            
        encMessg = rsa.encrypt(content, publicKey)
            
        with open(encFilename, "wb") as file0:
            file0.write(encMessg)
            
        print("File successfully encoded.")
            
        print(f"Your Private Key object: {privateKey}")
            
    case "d":
        decFilename = input("Enter the name for the file to decrypt: ")
    
        with open(decFilename, "rb") as file1:
            c = file1.read()
            
        try:
            # Decrypting using the persistent private key
            decMessg = rsa.decrypt(c, privateKey)
            
            with open(decFilename, "wb") as file1:
                file1.write(decMessg)
            print(f"File decoded successfully.")
            
        except rsa.DecryptionError:
            print("Error: The key does not match this file!")
            
    case _:
        print("Enter e or d: ")
 

    

    
    
    
        
    

