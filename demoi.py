
from hashlib import md5


def md5_encrypt(pwd: str):
    salt = 'dnkjsna234adfa./'
    method = md5(salt.encode('utf8'))
    method.update(pwd.encode("utf8"))
    encrypt_pwd = method.hexdigest()
    print(encrypt_pwd)
    return encrypt_pwd

md5_encrypt('1233s')
