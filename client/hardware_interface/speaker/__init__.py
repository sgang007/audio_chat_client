import platform
from .linux_speaker import LinuxSpeaker

if 'linux' in platform.system().lower():
    Speaker = LinuxSpeaker
else:
    raise Exception("Platform not Supported")

__all__=['Speaker']