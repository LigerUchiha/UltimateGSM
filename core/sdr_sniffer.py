import subprocess
import os

RAINBOW_TABLE_PATH = "data/rainbow_tables/"
CAPTURED_FILE = "data/capture.cfile"

def run_kraken():
    print("[*] Running Kraken against A5/1 ciphered capture...")
    try:
        subprocess.run([
            './kraken',
            CAPTURED_FILE,
            RAINBOW_TABLE_PATH
        ])
    except FileNotFoundError:
        print("[!] Kraken binary not found. Make sure it's compiled and in the root dir.")
    except Exception as e:
        print(f"[!] Kraken failed: {e}")

def decrypt_a51(key):
    print(f"[*] Using key {key} to decrypt A5/1 stream...")
    # Placeholder: Decryption logic (AES ECB post-Kraken)
    # You'd use a GSMTAP-compatible parser here to decode bursts using the key

def run():
    print("[*] Starting A5/1 cracking module...")
    run_kraken()
    # Assume key was extracted and is stored
    dummy_key = "FAKEKEY12345678"
    decrypt_a51(dummy_key)
