import pyaudio
import wave
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

class Audio:
    """wrapper for easy audio files manipulation."""
    def __init__(self):
        return

    def read(self, filename, chunk_size=CHUNK_SIZE):
        wf = wave.open(filename, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        data = wf.readframes(CHUNK_SIZE)
        while data != '':
            yield data
            data = wf.readframes(CHUNK_SIZE)

if __name__ == '__main__':
    a = Audio()
    a.

    
        


# CHUNK = 44100
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"

# p = pyaudio.PyAudio()

# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)

# print("* recording")

# stream.start_stream()

# # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
# def get_data(i):
    
#     ax.cla()
#     ax.plot(data)

# def init():
#     ax.set_ylim(-1e5, 1e5)
#     ax.set_xlim(0, 44100)
#     del xdata[:]
#     del ydata[:]
#     line.set_data(xdata, ydata)
#     return line,

# fig, ax = plt.subplots()
# line, = ax.plot([], [], lw=2)
# xdata, ydata = [], []

# def run(i):
#     ydata = np.frombuffer(stream.read(44100), dtype=np.int16)
#     xdata = np.arange(len(ydata))
#     print(ydata)
#     line.set_data(xdata, ydata)
#     return line,

# ani = FuncAnimation(fig, run, interval=1000, init_func=init, blit=True)

# plt.show()

# print("* done recording")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
