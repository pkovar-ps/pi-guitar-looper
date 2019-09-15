import threading
import soundfile
import sounddevice as sd
import soundfile as sf

data, fs = sf.read("audio_samples/tick.wav", dtype='float32')
data2, fs2 = sf.read("audio_samples/tock.wav", dtype='float32')
status = sd.wait()
tick = 1
count = 4

class Metronome(threading.Thread):


    __init__(self, bpm = 100):
        self.bpm = bpm
        self.time = 60/self.bpm


    def run():
        

    def beat():
        sd.play(data, fs)
        print(tick)
        if tick == 1:
            sd.play(data2, fs2)
        else:
            sd.play(data, fs)

        if tick == count:
            tick = 0
        tick += 1
        t = threading.Timer(time, beat)
        t.start()







t = threading.Timer(time, beat)
t.start() # after 30 seconds, "hello, world" will be printed