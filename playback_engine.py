"""PyAudio Example: Play a wave file (callback version)."""

import pyaudio
import wave
import time
import sys
import numpy
import threading

class AudioPlayback(threading.Thread):
    CHUNK = 1024

    def __init__(self, track):
        threading.Thread.__init__(self)
        self.loop_cnt = 1
        self.wfs = [] # array of waveforms
        self.p = None
        self.stream = None
        self.run_flag = False
        self.initiate(track)
        self.wav_frames = self.wfs[0].getnframes()

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
    
    def run(self):
        self.play()
        while self.run_flag:    
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

    def get_progress(self):
        return (self.wfs[0].tell() * 100) / self.wav_frames


audioPlayback = AudioPlayback("audio_samples/sample.wav")
'''
audioPlayback = AudioPlayback("audio_samples/multitrack/03_Hat.wav")
audioPlayback.add_track("audio_samples/multitrack/02_Snare.wav")
'''
audioPlayback.start()
print("Initiated")

audioPlayback.play()
print("Playback started")

while audioPlayback.stream.is_active():
    time.sleep(0.1)
    print("Loop:", audioPlayback.loop_cnt, "Progress: ", audioPlayback.get_progress(), " %")
    if audioPlayback.loop_cnt == 2:
        audioPlayback.stop()
        break
        
audioPlayback.join()
audioPlayback.destroy()

print("end main")