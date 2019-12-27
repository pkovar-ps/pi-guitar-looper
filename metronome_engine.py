import threading
import soundfile
import sounddevice as sd
import soundfile as sf
import time

class Metronome(threading.Thread):

    def __init__(self, bpm = 100):
        threading.Thread.__init__(self)
        self.bpm = bpm
        self.timing = 60/bpm
        self.tick = 1
        self.count = 4
        self.data, self.fs = sf.read("audio_samples/tick.wav", dtype='float32')
        self.data2, self.fs2 = sf.read("audio_samples/tock.wav", dtype='float32')
        self.run_flag = True

    def run(self):
        while self.run_flag:
            self.beat()
            time.sleep(self.timing)

    def play(self):
        self.run_flag = True

    def stop(self):
        self.run_flag = False

    def beat(self):
        #print(self.tick)
        if self.tick == 1:
            sd.play(self.data2, blocking=False)
        else:
            sd.play(self.data, blocking=False)

        if self.tick == self.count:
            self.tick = 0
        self.tick += 1

    def set_tempo(self, bpm):
        self.bpm = bpm
        self.timing = 60/bpm
        print("Timing: ", self.timing)


metronome = Metronome()
metronome.start()

while True:
    tempo = int(input("Input tempo: "))
    metronome.set_tempo(tempo)
