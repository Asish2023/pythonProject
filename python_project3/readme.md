# Asymmetric File Encoder & Decoder (RSA) in Python

This project demonstrates **asymmetric encryption and decryption** using RSA in Python.  
It allows you to encrypt and decrypt files using a **public/private key pair** stored in `.PEM` format.

The project uses the `rsa` Python library and focuses on understanding how public-key cryptography works at a practical level.

---

## Features

- Generates RSA public and private keys (1024-bit)
- Saves keys securely in `.pem` files
- Encrypts a file using the **public key**
- Decrypts the file using the **private key**
- Demonstrates core concepts of asymmetric encryption

---

## Requirements

- Python 3.x
- `rsa` library

Install the required dependency:
pip install rsa

1. Files Overview
    asymm_encoder.py
    - Generates RSA keys and encrypts a file using the public key.

    asymm_decoder.py
    - Loads existing RSA keys and decrypts a file using the private key.

    public.pem
    - Stores the RSA public key (generated automatically).

    private.pem
    - Stores the RSA private key (generated automatically).

2. How It Works
    a. Encryption Flow
    - Generate a public/private RSA key pair

    - Save keys in .PEM format

    - Read the target file in binary mode

    - Encrypt file contents using the public key

    - Overwrite the original file with encrypted data

    b. Decryption Flow
    - Load existing .PEM key files

    - Read the encrypted file in binary mode

    - Decrypt the contents using the private key

    - Restore the original file contents

3. Usage
Encrypt a File
- Run the encoder script:

python asymm_encoder.py
When prompted, enter the filename or full path of the file you want to encrypt.

- Decrypt a File
Run the decoder script:

python asymm_decoder.py
- When prompted, enter the filename or full path of the encrypted file.

# Important Notes
RSA encryption has size limits. This approach works best for small files.

In real-world applications, RSA is typically used to encrypt symmetric keys, not entire files.

Keep your private.pem file secure. Anyone with access to it can decrypt your data.

# Learning Goals
Understand asymmetric encryption concepts

Work with RSA key pairs and .PEM files

Explore how encryption and decryption work at the file level

Build foundational knowledge for cryptography and cybersecurity projects

# Credits
Inspired and guided by tutorials from NeuralNine on YouTube.
Excellent explanations of cryptography concepts and Python implementations.

# Disclaimer
This project is for educational purposes only and is not intended for production-level security use.

