import recorder
import music_note_detector

if __name__ == "__main__":
    recognized_notes = []
    for x in range(10):
        sound = recorder.record()
        note = music_note_detector.note_detect(sound)
        recognized_notes.append(note)
        print("\nDetected Note = " + str(note))
    
    print(str(recognized_notes))
    

