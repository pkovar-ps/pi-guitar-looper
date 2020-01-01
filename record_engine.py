import subprocess

class Recorder():

    recording = True

    def __init__(self):
        self.recording = True
        self.p = None

    def start(self, name):
        cmd = 'arecord -f cd ' + str(name) + '.wav'
        self.p = subprocess.Popen("exec " + cmd, stdout=subprocess.PIPE, shell=True)
        recording = False
        
    def stop(self):
        self.p.kill()
