import uuid
import hashlib

def setPass(password):
    salt = uuid.uuid4().hex
    encrypt=hashlib.sha512(salt.encode()+password.encode()).hexdigest() + ':' +salt
    return encrypt
def checkPass(password,encrypt):
    p , salt = encrypt.split(":")
    ch= hashlib.sha512(salt.encode()+password.encode()).hexdigest()
    return p == ch

print("Please enter password you want to set : ")
password=input()
encrypt=setPass(password)
if checkPass(password,encrypt):
    print("Password Match")