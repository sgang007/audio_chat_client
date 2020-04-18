from speech_recognition import AudioData
import pyaudio
import wave
CHUNK_SIZE = 1024


class Audio(AudioData):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = 0

    def getnchannels(self):
        return 1

    def getframerate(self):
        return self.sample_rate

    def getsampwidth(self):
        return self.sample_width

    def readframes(self, chunk_size):
        chunk = self.frame_data[self.position: self.position+chunk_size]
        self.position = self.position + chunk_size
        return chunk


class LinuxSpeaker:
    chunk = CHUNK_SIZE

    def __init__(self, data, width=None, rate=None):
        """ Init audio stream """
        self.p = pyaudio.PyAudio()
        if type(data) == bytes:
            self.data = Audio(data,
                              sample_rate=int(rate),
                              sample_width=int(width)
                              )
        else:
            self.data = wave.open(data, 'rb')

    def __enter__(self):
        self.stream = self.p.open(
            format=self.p.get_format_from_width(self.data.getsampwidth()),
            channels=self.data.getnchannels(),
            rate=self.data.getframerate(),
            output=True
        )
        return self

    def play(self):
        """ Play entire file """
        data = self.data.readframes(self.chunk)
        while data:
            self.stream.write(data)
            data = self.data.readframes(self.chunk)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

