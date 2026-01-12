# core/hasher.py

import hashlib


def calculate_sha256(file_path: str) -> str | None:
    """
    Calcula o hash SHA256 de um arquivo.
    Retorna o hash em hexadecimal ou None em caso de erro.
    """
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for block in iter(lambda: file.read(65536), b""):
                sha256.update(block)

        return sha256.hexdigest()

    except PermissionError:
        return None
    except FileNotFoundError:
        return None
    except Exception:
        return None
