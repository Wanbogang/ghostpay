# Demo receiver: isi variabel di bawah dengan hasil dari sender_example.py
from dh_shared import shared_secret_bytes, derive_sym_key
from encrypt import decrypt_message
from onetime_key import derive_one_time_keypair

# --- ISI MANUAL (copy dari output sender_example) ---
recv_view_priv = "<ISI_VIEW_PRIVATE_DARI_SENDER_OUTPUT>"
ephemeral_pub_b58 = "<ISI_EPHEMERAL_PUB_DARI_SENDER>"
cipher_b64 = "<ISI_CIPHER_B64_DARI_SENDER>"
# ----------------------------------------------------

def run():
    ss = shared_secret_bytes(recv_view_priv, ephemeral_pub_b58)
    sym = derive_sym_key(ss)
    plaintext = decrypt_message(sym, cipher_b64)
    print("Decrypted memo:", plaintext)

    # derive one-time private (untuk klaim jika perlu)
    ot_sk_b58, ot_pk_b58 = derive_one_time_keypair(ss)
    print("Derived one-time private (impornya ke wallet jika perlu):", ot_sk_b58)
    print("Derived one-time public:", ot_pk_b58)

if __name__ == "__main__":
    run()
