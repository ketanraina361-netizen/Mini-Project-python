import random
import string

chars = string.ascii_letters + string.digits     #Generate Password
password = ""
for i in range(8):
    password += random.choice(chars)
print("Generated Password:", password)

class PasswordError(Exception):        #Custom Exception
    pass

try:
    p = input("Enter Password: ")      #Validate Password
    if len(p) < 8:
        raise PasswordError("Password is too short")
    print("Password is Valid")

except PasswordError as e:
    print(e)