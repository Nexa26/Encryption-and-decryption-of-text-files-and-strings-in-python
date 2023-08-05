
from cryptography.fernet import Fernet

from key_file import key
f = Fernet(key)

n=input("Enter the name of the file to be encrypted:")
print()
with open(n, 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)
n1=input("Enter the name of the encrypted file:")
print()
with open (n1, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
print("File has been encrypted")
print()
f = Fernet(key)
with open(n1, 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)
m1=input("Enter the name of the decrypted file:")
with open(m1, 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
print()
print("File has been decrypted")


