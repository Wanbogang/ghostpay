import streamlit as st
from keygen import gen_x25519_keypair
from dh_shared import shared_secret_bytes, derive_sym_key
from onetime_key import derive_one_time_keypair
from encrypt import encrypt_message, decrypt_message

st.title("GhostPay — Demo")
st.header("1) Generate receiver view key")
if st.button("Generate view key"):
    sk, pk = gen_x25519_keypair()
    st.code(f"view_private: {sk}\nview_public: {pk}")

st.header("2) Sender: create one-time addr & encrypted memo")
recv_pub = st.text_input("Receiver view_public")
msg = st.text_input("Message", "Hello from GhostPay")
if st.button("Create & Encrypt"):
    if not recv_pub:
        st.error("Paste receiver view_public first")
    else:
        # generate ephemeral
        from nacl.public import PrivateKey
        import base58
        ephemeral = PrivateKey.generate()
        ephemeral_pk = base58.b58encode(ephemeral.public_key.encode()).decode()
        ss = shared_secret_bytes(base58.b58encode(ephemeral.encode()).decode(), recv_pub)
        sym = derive_sym_key(ss)
        ot_sk, ot_pk = derive_one_time_keypair(ss)
        cipher = encrypt_message(sym, msg)
        st.success("One-time address & encrypted memo created")
        st.write("ephemeral_pub::cipher_b64 ->")
        st.code(f"{ephemeral_pk}::{cipher}")
        st.write("one-time public:", ot_pk)
        st.write("one-time private (keep secret):", ot_sk)

st.header("3) Receiver: decrypt memo")
recv_priv = st.text_input("Receiver view_private for decrypt")
ephemeral_pair = st.text_input("Ephemeral::Cipher")
if st.button("Decrypt"):
    try:
        e_pub, c_b64 = ephemeral_pair.split("::")
        ss = shared_secret_bytes(recv_priv, e_pub)
        sym = derive_sym_key(ss)
        pt = decrypt_message(sym, c_b64)
        ot_sk, ot_pk = derive_one_time_keypair(ss)
        st.success("Decrypted")
        st.write("Message:", pt)
        st.write("Derived one-time private (for claim):", ot_sk)
    except Exception as e:
        st.error(str(e))
