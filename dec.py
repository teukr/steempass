from cryptography.fernet import Fernet
import base64

def _input(msg):
    return raw_input(msg)

master_key = base64.b64encode(_input('master key:'))
password   = _input('password to encrypt:')

encode_key = master_key[:32]
nopad_key = encode_key.replace('=','X')

cipher_key = '1V2RKQj0crfh1finQsJYCCuWuflcW3ECSf47UC2bG4E='
cipher_key = nopad_key + cipher_key[len(nopad_key):]
cipher = Fernet(cipher_key)
decrypted_text = cipher.decrypt(password)
print(decrypted_text)