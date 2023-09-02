# 1. Record for 1 min.
# 2. Find note.
# 3. Display note.
import recorder
import music_note_detector_test

if __name__ == "__main__":
    sample_width, frames = recorder.record()
    note = music_note_detector_test.note_detect(frames, sample_width)
    print("\n\tDetected Note = " + str(note))
    

