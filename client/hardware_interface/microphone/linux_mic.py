from speech_recognition import Microphone, Recognizer
from .base_mic import BaseMic


class LinuxMic(BaseMic):
    def __init__(self, *args, **kwargs):
        self.source = Microphone(device_index=kwargs.get('device_index') or None,
                                 sample_rate=kwargs.get('sample_rate') or 16000)
        self.recognizer = Recognizer()
        super().__init__(*args, **kwargs)

    @classmethod
    def get_mics(cls):
        return Microphone.list_microphone_names()

    def tune(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self.recognizer, key, val)

        with self.source as source:
            self.recognizer.adjust_for_ambient_noise(source)

    def listen(self, bg=False, callback=None, **kwargs):
        if bg and callback:
            return self.recognizer.listen_in_background(self.source, callback)
        else:
            with self.source as source:
                audio = self.recognizer.listen(source, **kwargs)
                return audio

    def record(self, duration=None, offset=None):
        return self.recognizer.record(self.source, duration, offset)

    def reset(self):
        self.source = None
        self.recognizer = None








