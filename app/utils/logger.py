import logging

def get_logger(name: str):
    logger = logging.getLogger(name)

    if not logging.getLogger().hasHandlers():
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

    return logger
