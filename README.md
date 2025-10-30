# GhostPay — Private P2P Payments (Stealth Addresses & Encrypted Memos)

**Tagline:** A Cypherpunk prototype for private P2P payments — stealth addresses + end-to-end encrypted memos.

---

## Summary
GhostPay is a prototype demonstrating how to:
- Derive a *one-time* (stealth) address using X25519 Diffie-Hellman,
- Encrypt transaction memos using XSalsa20-Poly1305 (PyNaCl),
- Allow the recipient to decrypt memos and derive a one-time private key to claim funds.

Goal: build an MVP for the DAWN Black Box hackathon focusing on message privacy and recipient obfuscation. **Note:** on-chain amounts are still visible in this prototype.

---

## Repository structure
ghostpay/
├── src/
│ ├── keygen.py
│ ├── dh_shared.py
│ ├── onetime_key.py
│ ├── encrypt.py
│ ├── sender_example.py
│ ├── receiver_example.py
│ └── auto_demo.py
├── requirements.txt
├── README.md
└── venv/

---

## Requirements
- Python 3.10+  
- Virtualenv (recommended)  
- (Optional for testnet) solana-cli & network access

Install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

How to run (Local demo — recommended)

Activate virtualenv:

source venv/bin/activate


Run the automatic demo (sender → receiver decrypt):

python src/auto_demo.py


Output will show:

Recipient view_private / view_public (demo)

ephemeral_pub and cipher_b64 (encrypted memo)

one-time public and one-time private (derived claim key)

Decrypted memo.

Manual alternative:

Run python src/sender_example.py — copy view_private, ephemeral_pub::cipher_b64.

Edit src/receiver_example.py and paste values into placeholders.

Run python src/receiver_example.py to see decryption.

Technical overview

Key model: each user has a view key (X25519).

Stealth derivation: sender generates ephemeral X25519 → DH(ephemeral_priv, view_pub) = shared secret → derive seed → create ed25519 one-time keypair.

Memo encryption: shared secret → KDF (SHA256) → symmetric key → SecretBox (XSalsa20-Poly1305) used to encrypt memo.

Claiming: the recipient who holds view_priv can compute shared secret from ephemeral included in memo, then derive the one-time private key to import/claim funds.

Limitations & security notes

On-chain amounts remain visible — this MVP does not hide transaction amounts.

Metadata leakage: memos placed on-chain can be observed; consider encrypted pointers to off-chain storage (IPFS) for improved privacy.

View key compromise: if view_priv leaks, an attacker can discover receipts (view-only). Do not publish private keys.

Private key handling: keep private keys safe and never commit them into the repository.

Roadmap (next steps)

Integrate Solana/DAWN devnet: convert one-time key → Solana keypair JSON & automate transfers.

Build a minimal indexer/inbox (RPC poller) for memos in EPH::CIPHER format.

Create a simple demo UI (Streamlit or React).

Add batching/coinjoin and zk-amounts to obscure amounts.

Submission artifacts

Repo: https://github.com/Wanbogang/ghostpay

Demo video (2–3 min): show generate key → send → decrypt → claim.

Slides: architecture, threat model, demo screenshots, roadmap.

Short security note: describe privacy limitations.

License

MIT — add LICENSE file if needed.

Author / Contact

Wanbogang — GitHub: https://github.com/Wanbogang

