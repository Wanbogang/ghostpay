from nacl.secret import SecretBox
from nacl.utils import random
import base64

def encrypt_message(sym_key, plaintext: str):
    box = SecretBox(sym_key)
    nonce = random(SecretBox.NONCE_SIZE)
    ct = box.encrypt(plaintext.encode(), nonce)  # includes nonce
    return base64.b64encode(ct).decode()

def decrypt_message(sym_key, ct_b64: str):
    box = SecretBox(sym_key)
    ct = base64.b64decode(ct_b64)
    pt = box.decrypt(ct)
    return pt.decode()
