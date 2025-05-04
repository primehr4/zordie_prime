# import logging
# import os
# from datetime import datetime

# def setup_logger(name: str, log_file: str) -> logging.Logger:
#     os.makedirs("logs", exist_ok=True)

#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)
#     logger.propagate = False  # prevent logging from affecting other loggers

#     log_path = os.path.join("logs", log_file)

#     # Prevent duplicate file handlers
#     if any(isinstance(h, logging.FileHandler) and h.baseFilename.endswith(log_file) for h in logger.handlers):
#         return logger

#     # Optional: Start-of-log timestamp line
#     if not os.path.exists(log_path):
#         with open(log_path, "a", encoding="utf-8") as f:
#             f.write(f"\n--- Log started at {datetime.now().isoformat()} ---\n")

#     file_handler = logging.FileHandler(log_path, mode='a', encoding='utf-8')
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)

#     return logger

import logging
import os
from datetime import datetime

def setup_logger(name: str, log_file: str) -> logging.Logger:
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False  # stop bubbling

    log_path = os.path.abspath(os.path.join("logs", log_file))

    # Check if exact file handler is already present
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler) and os.path.abspath(handler.baseFilename) == log_path:
            return logger  # Reuse existing

    # Create new handler if not found
    if not os.path.exists(log_path):
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"\n--- Log started at {datetime.now().isoformat()} ---\n")

    file_handler = logging.FileHandler(log_path, mode='a', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
