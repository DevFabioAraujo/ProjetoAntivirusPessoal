# core/scanner.py

import os
from antivirus.engine.detection import analyze_file
from antivirus.quarantine.quarantine_manager import QuarantineManager
from antivirus.core.logger import get_logger


logger = get_logger()


class FileScanner:
    def __init__(self):
        self.scanned_files = 0
        self.infected_files = []

    def scan_path(self, path: str):
        """
        Escaneia um arquivo ou diretório
        """
        if not os.path.exists(path):
            logger.error(f"Caminho não encontrado: {path}")
            return

        if os.path.isfile(path):
            self._scan_file(path)
        else:
            for root, _, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    self._scan_file(full_path)

    def _scan_file(self, file_path: str):
        """
        Escaneia um único arquivo
        """
        try:
            self.scanned_files += 1
            logger.info(f"Escaneando: {file_path}")

            result = analyze_file(file_path)

            if result["infected"]:
                logger.warning(f"AMEAÇA DETECTADA: {file_path}")
                self.infected_files.append({
                    "file": file_path,
                    "threat": result["threat"]
                })
                self.quarantine.quarantine_file(file_path, result["threat"])

        except PermissionError:
            logger.warning(f"Permissão negada: {file_path}")
        except Exception as e:
            logger.error(f"Erro ao escanear {file_path}: {e}")

    def summary(self):
        """
        Retorna resumo do scan
        """
        return {
            "scanned": self.scanned_files,
            "infected": len(self.infected_files),
            "details": self.infected_files
        }
