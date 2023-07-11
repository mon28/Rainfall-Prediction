import os
import sys
import logging
from datetime import datetime

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
filename = f"log_{CURRENT_TIME_STAMP}.log"
log_filepath = os.path.join(LOG_DIR, filename)

format = "[%(asctime)s %(name)s: %(levelname)s: %(module)s: %(message)s]"

logging.basicConfig(format=format,
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler(log_filepath),
                        logging.StreamHandler(sys.stdout)
                    ])
logger = logging.getLogger("rainfallPredictionLogger")