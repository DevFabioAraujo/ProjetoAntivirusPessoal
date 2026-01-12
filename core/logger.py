# core/logger.py

import logging

def get_logger():
    logging.basicConfig(
        filename="logs/antivirus.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("Antivirus")
