from daemons.prefab.run import RunDaemon
import time
from pynput.keyboard import GlobalHotKeys
from .tasks import *


class KeystrokeListener(RunDaemon):
    def run(self):
        COMBINATION = {
            '<ctrl>+<shift>+<f1>': record_and_send
        }
        with GlobalHotKeys(COMBINATION) as listener:
            listener.join()


