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


if __name__ == "__main__":
    folder_path = os.getcwd()
    file_name = folder_path + "\output.wav"
    print(file_name)

    audio_file = wave.open(file_name)
    note_detect(audio_file)