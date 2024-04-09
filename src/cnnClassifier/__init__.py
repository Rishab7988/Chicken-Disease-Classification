import os
import sys
import logging


# specifying the log format
# ascii time, levelname(info,debug,critical,info,), module(name of python file), message corr. to it
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# creating a directory to store the logs
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) # using StreamHandler we can print the logs on the terminal 
    ]
)

logger = logging.getLogger("cnnClassifierLogger")

# logger.info("Welcome to my custom logger")