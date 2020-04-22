import logging
import os
import sys
from .daemon import KeystrokeListener

if __name__ == '__main__':
    action = sys.argv[1]
    logfile = os.path.join(os.getcwd(), "audio_chat.log")
    pidfile = os.path.join(os.getcwd(), "audio_chat.pid")
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    d = KeystrokeListener(pidfile=pidfile)

    if action == "start":
        d.start()

    elif action == "stop":
        d.stop()

    elif action == "restart":
        d.restart()