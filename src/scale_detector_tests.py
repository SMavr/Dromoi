import scale_detector
import numpy as np
import pytest


@pytest.mark.parametrize("recognized_notes, scale, is_fisiko_armoniko_scale", [
    (np.array(["E","F","G"]), scale_detector.fisiko_minore_d_set, True),
    (np.array(["E", "F#", "G"]), scale_detector.fisiko_minore_d_set, False),
     (np.array(["E","F","G"]), scale_detector.armoniko_minore_d_set, True),
    (np.array(["E", "F", "C"]), scale_detector.armoniko_minore_d_set, False)
])

def test_is_scale(recognized_notes, scale, is_fisiko_armoniko_scale):
    result = scale_detector.is_scale(scale, recognized_notes)
    assert result == is_fisiko_armoniko_scale


@pytest.mark.parametrize("notes, output", [
    (np.array(["E4","F4","C#4"]), " Armoniko Minore D")

])

def test_detect_scale(notes, output):
    result = scale_detector.detect_scale(notes)
    assert result == output