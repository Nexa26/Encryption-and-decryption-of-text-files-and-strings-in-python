# Encryption and Decryption of Text and Files

This project is a GUI based application using tkinter that can encrypt and decrypt files and text.

## Installation

1. Install the cryptography and UPL packages using the following commands:

pip install cryptography\
pip install UPL


## Usage

cryptography is a package in python which provides cryptographic recipes and primitives to Python developers.
cryptography includes both high level recipes and low level interfaces to common cryptographic algorithms such as symmetric ciphers, message digests, and key derivation functions.\\ 

In this project we mainly use the fernet module from cryptography package
from cryptography.fernet import Fernet\\

We have a key_file which is used to generate the key for encryption and it is stored in my_key.key for a file
Similarly for strings we have key_string\\

file_ednc.py and string_ednc.py are where we give input for what text or file needs to be encrypted or decrypted and tdec.txt and tenc.txt are the selected files after decryption and encryption.\\


## Credits

This project was created by Paramatmuni Neha.
