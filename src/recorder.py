import pyaudio
import numpy as np

# Parameters for audio recording
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1              # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100              # Sample rate (samples per second)
CHUNK = 1024              # Number of frames per buffer
RECORD_SECONDS = 3       # Duration of recording in seconds


def record():

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open a stream to capture audio from the microphone
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    # Initialize an empty NumPy array to store the recorded audio
    audio_data = []

    # Record audio data in chunks
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        audio_data.append(data)

    print("Recording finished")

    # Close the audio stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Convert the recorded audio data into a NumPy array
    audio_array = np.frombuffer(b''.join(audio_data), dtype=np.int16)

    return audio_array


if __name__ == "__main__":
    test = record()
    print("Recording finished 2")