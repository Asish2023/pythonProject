# Simple File Encryption Tool

A Python-based utility that uses **Symmetric Key Encryption** (Fernet) to secure and restore files. This tool allows you to encrypt any file using a generated key and decrypt it back to its original state.

## 🛠 Features
- **Fernet (AES-128) Encryption:** Provides 128-bit AES encryption in CBC mode.
- **Key Generation:** Automatically generates a unique encryption key for every session.
- **In-place Encryption:** Overwrites the target file with encrypted data to ensure the original is not left exposed.

## 🚀 How to Use

### 1. Installation
Ensure you have the `cryptography` library installed:
bash
pip install cryptography


2. Encrypting a File
Run encrypt.py. You will be prompted for the filename you wish to lock.

The script reads the file.

It generates a key and saves it as fileKey.txt.

It replaces the file content with encrypted data.

3. Decrypting a File
Run decrypt.py. You will be prompted for:

The encrypted filename.

The key file (fileKey.txt).

The script uses the key to unlock the content and restores the file to its original format.

⚠️ Important Security Note
This project uses Symmetric Encryption.

The Key: The fileKey.txt is the only way to recover your data. If you lose this key, the data is gone forever.

Privacy: Do not share your fileKey.txt with anyone. Unlike a "Public Key," anyone with this file can decrypt your data.

📝 License
This project is open-source and available under the MIT License.
