fisiko_minore_d_set = set(["D","E", "F", "G", "A", "A#", "C", "D"])
armoniko_minore_d_set = set(["D","E", "F", "G", "A", "A#", "C#", "D"])

# Αρμονικό Μινόρε Re-
def detect_scale(notes):
    notes_without_octave = map(lambda note: note[:-1], notes)
    for i in notes_without_octave:
        print(i)
    output = ""
    if is_scale(fisiko_minore_d_set, notes_without_octave):
        output += " Fisiko Minore D"
    if is_scale(armoniko_minore_d_set, notes_without_octave):
        output += " Armoniko Minore D"

    return output    

    # for note in notes:
    #     note_without_octave = note[:-1]  # Remove the octave number from the note name
    #     if note_without_octave not in fisiko_minore_d_set:
    #         return False

    # return True


def is_scale(scale, notes):
    for note in notes:
        if note not in scale:
            return False
    return True