import numpy as np

fisiko_minore_d_set = set(["D","E", "F", "G", "A", "A#", "C", "D"])
armoniko_minore_d_set = set(["D","E", "F", "G", "A", "A#", "C#", "D"])

def detect_scale(notes):
    get_notes_without_octave = np.vectorize(lambda note: note[:-1])
    notes_without_octave = get_notes_without_octave(notes)

    output = ""

    if is_scale(fisiko_minore_d_set, notes_without_octave):
        output += " Fisiko Minore D"

    if is_scale(armoniko_minore_d_set, notes_without_octave):
        output += " Armoniko Minore D"

    return output

def is_scale(scale, notes):
    for note in notes:
        if note not in scale:
            return False
    return True