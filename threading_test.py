import threading
import soundfile
import sounddevice as sd
import soundfile as sf

data, fs = sf.read("audio_samples/beat.wav", dtype='float32')
sd.play(data, fs)
status = sd.wait()

bpm = 900
time = 60/bpm

def hello():
    print("hello, world")
    t = threading.Timer(1.0, hello)
    t.start()

def beat():
    sd.play(data, fs)
    t = threading.Timer(time, beat)
    t.start()

t = threading.Timer(time, beat)
t.start() # after 30 seconds, "hello, world" will be printed