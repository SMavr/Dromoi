import pyaudio
import wave
import audioop
import sys


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def record():

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("Start recording")

    frames = []

    try:
        while True:
            data = stream.read(CHUNK)
            print_volume(data)
            frames.append(data)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))


    sample_width = p.get_sample_size(FORMAT)

    stream.stop_stream()
    stream.close()
    p.terminate()

    
    return sample_width, frames


def record_to_file(file_path):
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(CHANNELS)
    sample_width, frames = record()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def print_volume(data:bytes):
    rms = audioop.rms(data, 2)
    print(' ' * 20, end='\r')
    print('#' * int((rms/500)), end='\r')
    

if __name__ == '__main__':
    print('#' * 80)
    print("Please speak inot the microphone")
    print("Press Ctrl+C to stop recording")

    record_to_file('output.wav')

    
    print("Result written to output.wav")
    print('#' * 80)