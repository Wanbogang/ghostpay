# GhostPay v0.1.0 — Release notes

## Summary
Initial prototype release:
- Core crypto primitives: X25519 DH, one-time ed25519 derivation.
- Encrypted memos via PyNaCl SecretBox (XSalsa20-Poly1305).
- auto_demo.py: end-to-end local demo.
- Streamlit UI: interactive demo (generate, send/encrypt, receive/decrypt).
- Unit test + GitHub Actions CI.
- Packaging: pyproject.toml + setup.cfg (editable install).
- MIT License + CONTRIBUTING guidelines.

## How to test
1. Clone repo & create venv.
2. `pip install -r requirements.txt` and `pip install -e .`
3. `python src/auto_demo.py` or `streamlit run src/app.py`

## Notes / Limitations
- Amounts are visible on-chain (MVP does not hide amounts).
- Memo stored in plain tx memo in demo; consider IPFS + encrypted pointer for production.
- No claim smart contract included; one-time private key derivation is shown as proof-of-concept.

