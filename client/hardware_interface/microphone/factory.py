from .linux_mic import LinuxMic
import platform


def get(*args, **kwargs):
    if 'linux' in platform.system().lower():
        l = LinuxMic(*args, **kwargs)
        l.tune(**kwargs)
        return l
    else:
        raise Exception("Platform not supported yet")