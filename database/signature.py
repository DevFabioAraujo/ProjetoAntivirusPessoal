# database/signatures.py

import json
import os

SIGNATURES_FILE = "database/signatures.json"


def load_signatures():
    if not os.path.exists(SIGNATURES_FILE):
        return set()

    with open(SIGNATURES_FILE, "r") as file:
        data = json.load(file)
        return set(data.get("hashes", []))


def is_malicious_hash(file_hash: str) -> bool:
    signatures = load_signatures()
    return file_hash in signatures
