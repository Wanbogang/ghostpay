# Demo sender: buat ephemeral, derive one-time address, encrypt memo
from keygen import gen_x25519_keypair
from dh_shared import shared_secret_bytes, derive_sym_key
from onetime_key import derive_one_time_keypair
from encrypt import encrypt_message
import base58
from nacl.public import PrivateKey

def run_sender_demo():
    # Untuk demo lokal: kita buat receiver view key di sini.
    recv_sk_b58, recv_pk_b58 = gen_x25519_keypair()
    print("=== RECIPIENT VIEW KEY (demo) ===")
    print("view_private:", recv_sk_b58)
    print("view_public :", recv_pk_b58)
    print("=================================")

    # Sender generates ephemeral key
    ephemeral = PrivateKey.generate()
    ephemeral_sk_b58 = base58.b58encode(ephemeral.encode()).decode()
    ephemeral_pk_b58 = base58.b58encode(ephemeral.public_key.encode()).decode()
    print("\nEPHEMERAL pub (sertakan ini di memo):", ephemeral_pk_b58)

    # Compute shared secret S = DH(ephemeral_priv, recv_view_pub)
    ss = shared_secret_bytes(ephemeral_sk_b58, recv_pk_b58)
    sym = derive_sym_key(ss)

    # Derive one-time address (public)
    ot_sk_b58, ot_pk_b58 = derive_one_time_keypair(ss)
    print("ONE-TIME address (pub):", ot_pk_b58)
    print("ONE-TIME private (priv - simpan aman jika ingin klaim):", ot_sk_b58)

    # Encrypt memo
    cipher_b64 = encrypt_message(sym, "Halo, ini pesan rahasia untukmu")
    print("\nEncrypted memo (simpan di tx memo):", cipher_b64)

    print("\n--- Copy these to receiver to decrypt ---")
    print("ephemeral_pub::cipher_b64 ->")
    print(f"{ephemeral_pk_b58}::{cipher_b64}")

if __name__ == "__main__":
    run_sender_demo()
