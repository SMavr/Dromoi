# 1. Record for 1 min.
# 2. Find note.
# 3. Display note.
import recorder
import music_note_detector

if __name__ == "__main__":
    sound = recorder.record()
    note = music_note_detector.note_detect(sound)
    print("\nDetected Note = " + str(note))
    

