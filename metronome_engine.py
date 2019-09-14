import pyaudio
import wave
import time
import sys
import numpy
import threading

class Metronome(threading.Thread):
    CHUNK = 1024

    def __init__(self):
        threading.Thread.__init__(self)
        self.loop_cnt = 0
        self.p = None
        self.stream = None
        self.run_flag = True
        self.wf = None

    def initiate(self, track):
        self.p = pyaudio.PyAudio()
        self.wf = wave.open(track, 'rb')
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                channels=self.wf.getnchannels(),
                rate=self.wf.getframerate(),
                output=True)

    def play(self):
        data = self.wf.readframes(self.CHUNK)
        data_sum = numpy.fromstring(data, numpy.int16)
        data_sum = (data_sum).astype(numpy.int16)
        self.stream.write(data_sum.tostring())
        if (self.run_flag == True):
            self.start_playing(1)
        
    def stop(self):
        self.run_flag = False
        
    def destroy(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        for wf in self.wfs:
            wf.close()
        self.p.terminate()

    def start_playing(self, tempo):
        timer = threading.Timer(tempo, self.play)
        timer.start()


metronome = Metronome()
metronome.start()

metronome.initiate("audio_samples/beat.wav")

metronome.start_playing(1)

print("Playback started")


metronome.join()
print("end main")