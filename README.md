[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# 🕶️ GhostPay — Private P2P Payments (Stealth Addresses & Encrypted Memos)

**GhostPay** is a cyberpunk-inspired prototype for private peer-to-peer payments, built with Python.  
It demonstrates **stealth address derivation**, **end-to-end encrypted memos**, and **claimable transaction links** — designed to explore privacy concepts for next-gen payment rails.

---

## 🧩 Key Features

- 🔐 One-time **stealth address** generation using X25519 (Diffie-Hellman)
- 📨 **Encrypted memos** secured with ChaCha20-Poly1305 (PyNaCl)
- 🧾 **Claimable payment links** to simulate off-chain message passing
- ⚙️ Modular cryptographic primitives — easy to integrate or extend
- 🧠 Designed as a learning and research prototype (not production code)

---

## 🗂️ Repository Structure
ghostpay/

├── src/

│ ├── keygen.py # Generate base + ephemeral key pairs

│ ├── dh_shared.py # Compute shared secrets via X25519

│ ├── encrypt.py # Encrypt/decrypt memos (ChaCha20-Poly1305)

│ ├── onetime_key.py # Derive stealth address for each payment

│ ├── sender_example.py # Example: sender encrypts & sends payment

│ └── receiver_example.py # Example: receiver decrypts memo

├── .gitignore

├── requirements.txt

└── README.md

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Wanbogang/ghostpay.git
cd ghostpay
```
### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # (Linux / macOS)
# or
venv\Scripts\activate      # (Windows)
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run examples
Sender encrypts and creates payment link
```bash
python src/sender_example.py
```

Receiver decrypts and reads memo
```bash
python src/receiver_example.py
```

# 🧠 How It Works

1. Key Generation — each participant (Alice & Bob) generates a base X25519 key pair.

2. Stealth Address Derivation — Alice uses Bob’s public key and a fresh ephemeral key to derive a one-time address.

3. Memo Encryption — Alice encrypts the transaction memo using the shared secret (Diffie-Hellman output).

4. Claim Process — Bob scans for payments addressed to his derived keys and decrypts memos using his private base key.

## 🧪 Cryptographic Primitives

| Component      | Algorithm           | Library       |
|----------------|---------------------|----------------|
| Key Exchange   | X25519              | PyNaCl         |
| Encryption     | ChaCha20-Poly1305   | PyNaCl         |
| Hashing        | SHA-256             | hashlib        |
| Encoding       | Base58 / Base64     | Python stdlib  |

# 🛡️ Disclaimer

GhostPay is an educational prototype, not a financial product.
Do NOT use it for real transactions or sensitive data.
The project aims to explore privacy-enhancing cryptography concepts.

# 🧑‍💻 Author

Wanbogang Labs
Cyberpunk sandbox for next-generation privacy systems.
GitHub: https://github.com/Wanbogang



