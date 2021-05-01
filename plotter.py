import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import pyaudio
import wave

class Audio:
    """wrapper for easy audio files manipulation."""
    def __init__(self):
        return

    def read(self, filename, chunk_size):
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(chunk_size)
        while len(data) != 0:
            converted_data = np.frombuffer(data, dtype=np.int16)
            yield converted_data
            data = wf.readframes(chunk_size)
        stream.stop_stream()
        stream.close()
        p.terminate()
            
    def record(self, FORMAT, CHANNELS, RATE, CHUNK):
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True)
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            yield data

# def plot(filename, blit=True):
    
if __name__ == '__main__':
    w = Audio()
    time_start = time.time()
    i = 0
    fig, ax = plt.subplots()
    for frame in w.read('sample.wav', 4410):
        i += 1
        ax.cla()
        ax.plot(frame)
        plt.pause(0.001)
    time_elapsed = time.time() - time_start
    print(f'{i} frames in {time_elapsed:.2f} seconds --- {i//time_elapsed} fps')

