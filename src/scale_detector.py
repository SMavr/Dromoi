fisiko_minore_d_set = set(["D","E", "F", "G", "A", "A#", "C", "D"])

def detect_scale(notes):
    for note in notes:
        note_without_octave = note[:-1]  # Remove the octave number from the note name
        if note_without_octave not in fisiko_minore_d_set:
            return False

    return True