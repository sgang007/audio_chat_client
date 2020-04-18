from client.hardware_interface.microphone import Microphone
from client.hardware_interface.speaker import Speaker
import bz2
from datetime import datetime
import json

SECRET_KEY = 'test'

def record_and_send():
    audio = Microphone().listen()
    compressed_data = {
        'data': bz2.compress(audio.frame_data),
        'rate': audio.sample_rate,
        'width': audio.sample_width
    }
    #TODO: Compress, encrypt and send
