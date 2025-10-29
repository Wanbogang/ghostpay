#!/usr/bin/env python3
# auto_demo: jalankan sender_example.py, parse output, lalu dekripsi langsung
import subprocess, re, sys
from dh_shared import shared_secret_bytes, derive_sym_key
from encrypt import decrypt_message
from onetime_key import derive_one_time_keypair

def run_sender_and_capture():
    p = subprocess.run([sys.executable, "src/sender_example.py"], capture_output=True, text=True)
    out = p.stdout
    # print(out)  # debug
    # capture view_private
    m_view = re.search(r"view_private:\s*([A-Za-z0-9+/=]{20,})", out)
    # capture ephemeral::cipher line (last occurrence)
    m_pair = None
    for line in out.splitlines():
        if "::" in line and not line.startswith("http"):
            # naive split on ::
            parts = line.strip().split("::")
            if len(parts) == 2:
                m_pair = parts
    if not m_view or not m_pair:
        print("Gagal parse output sender. Berikut output:\n", out)
        sys.exit(1)
    view_priv = m_view.group(1).strip()
    ephemeral_pub = m_pair[0].strip()
    cipher_b64 = m_pair[1].strip()
    return view_priv, ephemeral_pub, cipher_b64, out

def decrypt_flow(view_priv, ephemeral_pub, cipher_b64):
    ss = shared_secret_bytes(view_priv, ephemeral_pub)
    sym = derive_sym_key(ss)
    pt = decrypt_message(sym, cipher_b64)
    ot_sk, ot_pk = derive_one_time_keypair(ss)
    return pt, ot_sk, ot_pk

if __name__ == "__main__":
    v, e, c, out = run_sender_and_capture()
    print("\n--- Sender Output ---\n")
    print(out)
    print("\n--- Receiver auto-decrypt ---\n")
    plaintext, ot_sk, ot_pk = decrypt_flow(v, e, c)
    print("Decrypted memo:", plaintext)
    print("Derived one-time private:", ot_sk)
    print("Derived one-time public :", ot_pk)
