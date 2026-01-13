# quarantine/quarantine_manager.py

import os
import shutil
import json
from datetime import datetime
from antivirus.core.hasher import calculate_sha256
from antivirus.core.logger import get_logger

logger = get_logger()

QUARANTINE_DIR = "quarantine/storage"
METADATA_FILE = "quarantine/quarantine_index.json"


class QuarantineManager:

    def __init__(self):
        self.quarantine = QuarantineManager()
        os.makedirs(QUARANTINE_DIR, exist_ok=True)
        if not os.path.exists(METADATA_FILE):
            with open(METADATA_FILE, "w") as f:
                json.dump([], f)
      

    def quarantine_file(self, file_path: str, threat_name: str):
        try:
            file_hash = calculate_sha256(file_path)
            if not file_hash:
                return False

            quarantine_name = f"{file_hash}.quarantine"
            destination = os.path.join(QUARANTINE_DIR, quarantine_name)

            shutil.move(file_path, destination)

            self._save_metadata(
                original_path=file_path,
                quarantine_path=destination,
                threat=threat_name,
                hash=file_hash
            )

            logger.warning(f"Arquivo movido para quarentena: {file_path}")
            return True

        except Exception as e:
            logger.error(f"Erro na quarentena: {e}")
            return False

    def _save_metadata(self, original_path, quarantine_path, threat, hash):
        with open(METADATA_FILE, "r+") as f:
            data = json.load(f)
            data.append({
                "original_path": original_path,
                "quarantine_path": quarantine_path,
                "threat": threat,
                "hash": hash,
                "date": datetime.now().isoformat()
            })
            f.seek(0)
            json.dump(data, f, indent=4)
