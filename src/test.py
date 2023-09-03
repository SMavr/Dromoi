# 1. Record for 1 min.
# 2. Find note.
# 3. Display note.
import recorder_test
import music_note_detector_test

if __name__ == "__main__":
    sound = recorder_test.record()
    note = music_note_detector_test.note_detect_2(sound)
    print("\n\tDetected Note = " + str(note))
    

