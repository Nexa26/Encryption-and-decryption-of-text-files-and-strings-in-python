# Encryption and Decryption of Text and Files

This project is a GUI based application using tkinter that can encrypt and decrypt files and text.

## Installation

Install the cryptography and UPL packages using the following commands:

pip install cryptography\
pip install UPL


## Usage

1. Run the file cs_proj.py
2. Select if you want to encrypt text or files
3. For text 
4. Enter the text nd click on encrypt
For files
5. Select the file you want to encrypt
6. Give the name of the encrypted file 
7. And to decrypt 
8. Give the name of the decrypted file.


cryptography is a package in python which provides cryptographic recipes and primitives to Python developers.
cryptography includes both high level recipes and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions.

In this project we mainly use the fernet module from cryptography package
from cryptography.fernet import Fernet

We have a key_file which is used to generate the key for encryption and it is stored in my_key.key for a file
Similarly for strings we have key_string

file_ednc.py and string_ednc.py are where we give input for what text or file needs to be encrypted or decrypted and tdec.txt and tenc.txt are the selected files after decryption and encryption.


## Credits

This project was created by Paramatmuni Neha.
