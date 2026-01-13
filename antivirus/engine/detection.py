# engine/detection.py

from antivirus.core.hasher import calculate_sha256
from antivirus.database.signatures import is_malicious_hash


def analyze_file(file_path: str) -> dict:
    """
    Analisa um arquivo e retorna o resultado.
    """
    file_hash = calculate_sha256(file_path)

    if not file_hash:
        return {
            "infected": False,
            "threat": None
        }

    if is_malicious_hash(file_hash):
        return {
            "infected": True,
            "threat": "Malware.Signature.Detected"
        }

    return {
        "infected": False,
        "threat": None
    }
