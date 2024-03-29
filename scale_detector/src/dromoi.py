import constants
import recorder
import music_note_detector
import scale_detector


if __name__ == "__main__":
    recognized_notes = []
    for x in range(constants.NUMBER_OF_NOTES):
        sound = recorder.record()
        note = music_note_detector.note_detect(sound)
        recognized_notes.append(note)
        print("\nDetected Note = " + str(note))
    
    print(str(recognized_notes))

    print(scale_detector.detect_scale(recognized_notes))
    
    input("Press Enter to continue")