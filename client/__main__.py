import logging
import os
import sys
from .daemon import KeystrokeListener


def key_listener():
    action = sys.argv[1]
    pidfile = os.path.join(os.getcwd(), "key_listener.pid")
    logfile = os.path.join(os.getcwd(), "key_listener.log")
    logging.basicConfig(filename=logfile, level=logging.DEBUG)

    d = KeystrokeListener(pidfile=pidfile)
    if action == "start":
        d.start()
    elif action == "stop":
        d.stop()
    elif action == "restart":
        d.restart()


if __name__ == '__main__':
    key_listener()