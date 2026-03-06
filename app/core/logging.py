import logging
import sys
from pythonjsonlogger import jsonlogger

def setup_logging(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    
    formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger