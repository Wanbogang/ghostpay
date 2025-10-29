from nacl.public import PrivateKey
import base58

def gen_x25519_keypair():
    sk = PrivateKey.generate()
    pk = sk.public_key
    sk_b58 = base58.b58encode(sk.encode()).decode()
    pk_b58 = base58.b58encode(pk.encode()).decode()
    return sk_b58, pk_b58

if __name__ == "__main__":
    sk, pk = gen_x25519_keypair()
    print("view_private:", sk)
    print("view_public :", pk)
