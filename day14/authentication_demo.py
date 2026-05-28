#werkzeug - Lets understand hashing

from werkzeug.security import generate_password_hash, check_password_hash
password="hello123"
hashed=generate_password_hash(password)
print(hashed)
passwd = input("Enter Password:")
print(check_password_hash(hashed,passwd))