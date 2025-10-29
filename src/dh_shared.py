from nacl.bindings import crypto_scalarmult
import base58
import hashlib

def shared_secret_bytes(priv_b58, peer_pub_b58):
    priv = base58.b58decode(priv_b58)
    peer = base58.b58decode(peer_pub_b58)
    ss = crypto_scalarmult(priv, peer)   # 32 bytes
    return ss  # raw bytes

def derive_sym_key(ss_bytes):
    # simple KDF: sha256
    return hashlib.sha256(ss_bytes).digest()  # 32 bytes
