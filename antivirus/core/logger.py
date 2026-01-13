# core/logger.py
import logging
import os


def get_logger():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    log_dir = os.path.join(base_dir, "logs")

    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "antivirus.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        encoding="utf-8"
    )

    return logging.getLogger("antivirus")
