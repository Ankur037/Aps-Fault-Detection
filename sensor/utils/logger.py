import logging
import os
from datetime import datetime

#Log File Name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

#Log Directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#Create Folder if not Available
os.makedirs(LOG_FILE_DIR, exist_ok=True)

#Log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level = logging.DEBUG,
)