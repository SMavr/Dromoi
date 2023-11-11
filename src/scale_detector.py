d_fisiko_armoniko_set = set(["D","E", "F", "G", "A", "A#", "C", "D"])

def detect_scale(notes):
    for note in notes:
        note_without_octave = note[:-1]  # Remove the octave number from the note name
        if note_without_octave not in d_fisiko_armoniko_set:
            return False

    return True