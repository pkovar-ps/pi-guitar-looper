"""PyAudio Example: Play a wave file (callback version)."""

import pyaudio
import wave
import time
import sys
import numpy
import threading


class AudioPlayback(threading.Thread):
    CHUNK = 1024

    def __init__(self):
        threading.Thread.__init__(self)
        self.loop_cnt = 0
        self.wfs = [] # array of waveforms
        self.p = None
        self.stream = None
        self.run_flag = True

    def add_track(self, track):
        print("Debug: adding track: " + track)
        self.wfs.append(wave.open(track, 'rb'))

    def initiate(self, track):
        self.add_track(track)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wfs[0].getsampwidth()),
                channels=self.wfs[0].getnchannels(),
                rate=self.wfs[0].getframerate(),
                output=True)

        while True: 
            if self.run_flag:
                data_sum = 0
                for wf in self.wfs:
                    data = wf.readframes(self.CHUNK)
                    if data == b'':
                        for wf in self.wfs:
                            wf.rewind()
                        self.loop_cnt += 1
                        data = wf.readframes(self.CHUNK)
                    data_sum += numpy.fromstring(data, numpy.int16)
                data_sum = (data_sum).astype(numpy.int16)
                self.stream.write(data_sum.tostring())

    def play(self):
        self.run_flag = True
        
    def stop(self):
        self.run_flag = False
        
    def destroy(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        for wf in self.wfs:
            wf.close()
        self.p.terminate()


audioPlayback = AudioPlayback()
audioPlayback.start()

audioPlayback.initiate("audio_samples/sample.wav")
audioPlayback.play()

print("Playback started")


wav_frames = audioPlayback.wfs[0].getnframes()
while audioPlayback.stream.is_active():
    time.sleep(1)
    print("Progress: " + str(round(((audioPlayback.wfs[0].tell() * 28)/wav_frames), 0)) + " leds")


audioPlayback.join()
print("end main")