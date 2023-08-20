import os
import wave
import math
import numpy as np
import struct
import matplotlib.pyplot as plt

def note_detect(audio_file):
    
    # Store sound file as a numpy array.
    file_length = audio_file.getnframes()
    sampling_frequency = audio_file.getframerate()

    sound = np.zeros(file_length) # Initializing array

    for i in range(file_length):
        wdata = audio_file.readframes(1)
        data = struct.unpack("<h", wdata)
        sound[i] = int(data[0])
    
    plt.plot(sound)
    plt.show()

    sound = np.divide(sound, float(2**15)) # Scaling it to 0 - 1
    counter = audio_file.getnchannels()

    plt.plot(sound)
    plt.show()

    # Applying FFT from numpy module
    fourier = np.fft.fft(sound)
    fourier = np.absolute(fourier)
    imax = np.argmax(fourier[0:int(file_length/2)]) # index of max element

    plt.plot(fourier)
    plt.show()



if __name__ == "__main__":
    folder_path = os.getcwd()
    file_name = folder_path + "\output.wav"
    print(file_name)

    audio_file = wave.open(file_name)
    note_detect(audio_file)