import keyboard
from metronome_engine import *
from playback_engine import *
from record_engine import *

metronome = Metronome(140)
recording = Recorder()

track_count = 0
is_playing = False

while True:
    if keyboard.is_pressed("r"):
        print("You pressed r")
        recording.start(track_count)
        track_count += 1
        time.sleep(0.5)

    if keyboard.is_pressed("s"):
        print("You pressed s")
        recording.stop()
        time.sleep(0.5)

    if keyboard.is_pressed("p"):
        print("You pressed p")
        audioPlayback = AudioPlayback("0.wav")
        is_playing = True
        audioPlayback.start()
        time.sleep(0.5)

    if keyboard.is_pressed("o"):
        print("You pressed o")
        is_playing = False
        audioPlayback.stop()
        time.sleep(0.5)

    if keyboard.is_pressed("e"):
        print("You pressed e")
        break

    

    if is_playing:
        time.sleep(0.2)
        print("Loop: %d | Progress: %.0f%% | Time: %.2fs" % (audioPlayback.loop_cnt, audioPlayback.get_progress(), audioPlayback.get_progress_sec()))

#audioPlayback = AudioPlayback("0.wav")
'''
audioPlayback = AudioPlayback("audio_samples/multitrack/03_Hat.wav")
audioPlayback.add_track("audio_samples/multitrack/02_Snare.wav")
'''

print("Initiated")

#audioPlayback.play()
#audioPlayback.start()
#metronome.start()
print("Playback started")


        
audioPlayback.join()
audioPlayback.destroy()

print("end main")