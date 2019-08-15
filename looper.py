import subprocess
import time
import psutil

loop = True;

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

def record_track(num):
    recorder = subprocess.Popen("arecord -f cd track_" + str(num) +".wav", stdout=subprocess.PIPE, shell=True)
    time.sleep(4)
    kill(recorder.pid)

def play_track(num):
    player = subprocess.Popen("mplayer sample.wav -loop 0", stdout=subprocess.PIPE, shell=True)

play_track(1)

while loop:
    None

kill(player.pid)
    