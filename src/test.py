import recorder
import music_note_detector

if __name__ == "__main__":
    for x in range(15):
        sound = recorder.record()
        note = music_note_detector.note_detect(sound)
        print("\nDetected Note = " + str(note))
    

