import numpy as np

fisiko_minore_d_set = set(["D","E", "F", "G", "A", "A#", "C", "D"])
armoniko_minore_d_set = set(["D","E", "F", "G", "A", "A#", "C#", "D"])
niaventi_d_set = set(["D", "E", "F", "G#", "A", "A#", "C#", "D"])
nigris_poimenikos_d_set = set(["D", "E", "F", "G#", "A", "B", "C", "D"])
hitzaz_d_set = set(["D", "D#", "F#", "G", "A", "A#", "C", "D"])
hitzaskiar_d_set = set(["D", "D#", "F#", "G", "A", "A#", "C#", "D"])
pireotikos_d_set = set(["D", "D#", "F#", "G#", "A", "A#", "C#", "D"])
fisiko_matzore_d_set = set(["D", "E", "F#", "G", "A", "B", "C#", "D"])
segiah_d_set = set(["D", "E", "F#", "G", "A", "B", "C#", "D"])
houzam_d_set = set(["D", "F", "F#", "G", "A", "A#", "C#", "D"])
ouzak_d_set = set(["D", "D#", "F", "G", "A", "A#", "C", "D"])

def detect_scale(notes):
    get_notes_without_octave = np.vectorize(lambda note: note[:-1])
    notes_without_octave = get_notes_without_octave(notes)

    output = ""

    if is_scale(fisiko_minore_d_set, notes_without_octave):
        output += " Fisiko Minore D"

    if is_scale(armoniko_minore_d_set, notes_without_octave):
        output += " Armoniko Minore D"

    if is_scale(niaventi_d_set, notes_without_octave):
        output += " Niaventi D"

    if (is_scale(nigris_poimenikos_d_set, notes_without_octave)):
         output += " Nigris, Poimenikos D"

    if (is_scale(hitzaz_d_set, notes_without_octave)):
         output += " Hitzaz D"

    if (is_scale(hitzaskiar_d_set, notes_without_octave)):
         output += " Hitzaskiar D"

    if (is_scale(pireotikos_d_set, notes_without_octave)):
         output += " Peirotikos D"

    if (is_scale(fisiko_matzore_d_set, notes_without_octave)):
         output += " Fisiko Matzore D"

    if (is_scale(segiah_d_set, notes_without_octave)):
         output += " Segiah D"

    if (is_scale(houzam_d_set, notes_without_octave)):
         output += " Houzam D"

    if (is_scale(ouzak_d_set, notes_without_octave)):
         output += " Ouzak D"

    else:
         output += " Test"
    return output

def is_scale(scale, notes):
    for note in notes:
        if note not in scale:
            return False
    return True