#!/usr/bin/env python

# Author: Muhammad Ahmad
# Email : muhammadahmadkon@gmail.com
# Date : 06 - Oct - 2023

# About: This file is write application log file.

# ========== Import modules ==========
import os
from datetime import datetime
from dotenv import load_dotenv

# Load the environment variables.
load_dotenv()


# ========== Write Log Function ==========
# This function will write the log to the log file.
# It will take two parameters:
# 1. log: The log to be written.
# 2. path: The path of the log file.
# It will return nothing.

def writeAppLog(log, path=os.getenv("APP_LOG_FILE")) -> None:
    
    """
    This function will write the log to the log file.
    
    It will take two parameters:
    1. log: The log to be written.
    2. path: The path of the log file.
    
    It will return nothing.
    """
    
    try:
        if not os.path.exists(path):
            dirName = os.path.dirname(path)
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            with open(path, "w") as log_file:
                log_file.write("")
        with open(path, "a") as log_file:
            logToWrite = f"[{datetime.now()}] {log}\n"
            log_file.write(logToWrite)
    except:
        pass # Because we don't want to write log file of the log file.