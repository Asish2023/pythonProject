# asymm_encoder.py
import rsa

public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))
    
with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))
    
textFile = input("Enter Filename or File path: ")

with open(textFile, "rb") as f:
    content = f.read()
    
enc_content = rsa.encrypt(content, public_key)

with open(textFile, "wb") as f:
    f.write(enc_content)
print("File encrypted successfully!")
