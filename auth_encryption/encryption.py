from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Encryption():
    def __init__(self, *args, **kwargs):
        self.encryption = Fernet('2cz1E7HqHZFNkqAJ6IfxoV4IMxFHrhN7md2PjRpb32Q=')

    def encrypt(self, data):
        cipher = data
        if type(data) is dict:
            cipher = str(data)
        try:
            return self.encryption.encrypt(cipher.encode()).decode()
        except:
            return False

    def decrypt(self, data):
        try:
            return self.encryption.decrypt(data.encode()).decode()
        except:
            return False
