from cryptography.fernet import Fernet
import base64

def _input(msg):
    return raw_input(msg)

master_key = _input('master key:')
password   = _input('password to encrypt:')

key_base64 = base64.b64encode(master_key)
encode_key = key_base64[:32]
nopad_key = encode_key.replace('=','X')

cipher_key = '1V2RKQj0crfh1finQsJYCCuWuflcW3ECSf47UC2bG4E='
cipher_key = nopad_key + cipher_key[len(nopad_key):]
cipher = Fernet(cipher_key)
encrypted_text = cipher.encrypt(password)
print('encrypted password\n' + encrypted_text) 