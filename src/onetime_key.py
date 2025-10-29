import hashlib
import base58
from nacl.signing import SigningKey

def derive_one_time_keypair(shared_secret_bytes):
    # seed = SHA256(shared || b'one-time')
    seed = hashlib.sha256(shared_secret_bytes + b"one-time").digest()
    # Use ed25519 SigningKey from seed (32 bytes)
    sk = SigningKey(seed)
    vk = sk.verify_key
    sk_b58 = base58.b58encode(sk.encode()).decode()
    vk_b58 = base58.b58encode(vk.encode()).decode()
    return sk_b58, vk_b58
