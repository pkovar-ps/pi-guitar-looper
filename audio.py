"""PyAudio Example: Play a wave file (callback version)."""

import pyaudio
import wave
import time
import sys
import numpy


CHUNK = 1024
loop_cnt = 0
wfs = []

wfs.append(wave.open("sample.wav", 'rb'))
'''
wfs.append(wave.open("multitrack/01_Kick.wav", 'rb'))
wfs.append(wave.open("multitrack/02_Snare.wav", 'rb'))
wfs.append(wave.open("multitrack/03_Hat.wav", 'rb'))
wfs.append(wave.open("multitrack/05_Bass.wav", 'rb'))
wfs.append(wave.open("multitrack/06_ElecGtr1.wav", 'rb'))
wfs.append(wave.open("multitrack/07_ElecGtr2.wav", 'rb'))
wfs.append(wave.open("multitrack/08_ElecGtr3.wav", 'rb'))
wfs.append(wave.open("multitrack/09_LeadVox.wav", 'rb'))
wfs.append(wave.open("multitrack/10_BackingVox1.wav", 'rb'))
wfs.append(wave.open("multitrack/11_BackingVox2.wav", 'rb'))
wfs.append(wave.open("multitrack/12_BackingVox3.wav", 'rb'))
wfs.append(wave.open("multitrack/13_BackingVox4.wav", 'rb'))
wfs.append(wave.open("multitrack/14_BackingVox5.wav", 'rb'))
'''

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream using callback (3)
stream = p.open(format=p.get_format_from_width(wfs[0].getsampwidth()),
                channels=wfs[0].getnchannels(),
                rate=wfs[0].getframerate(),
                output=True)

while True:
    data_sum = 0
    for wf in wfs:
        data = wf.readframes(CHUNK)
        if data == b'':
            for wf in wfs:
                wf.rewind()
            loop_cnt += 1
            data = wf.readframes(CHUNK)
        data_sum += numpy.fromstring(data, numpy.int16)
    data_sum = (data_sum).astype(numpy.int16)
    stream.write(data_sum.tostring())

stream.close()
player.terminate()

# start the stream (4)
#stream.start_stream()

# wait for stream to finish (5)
wav_frames = wfs[0].getnframes()
while stream.is_active():
    time.sleep(1)
    print("Progress: " + str(round(((wfs[0].tell() * 28)/wav_frames), 0)) + " leds")

# stop stream (6)
stream.stop_stream()
stream.close()
for wf in wfs:
    wf.close()

# close PyAudio (7)
p.terminate()



