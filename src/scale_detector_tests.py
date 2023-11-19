import scale_detector
import numpy as np
import pytest


@pytest.mark.parametrize("recognized_notes, is_fisiko_armoniko_scale", [
    (np.array(["E","F","G"]), True),
    (np.array(["E", "F#", "G"]), False)
])

def test_is_scale(recognized_notes, is_fisiko_armoniko_scale):
    result = scale_detector.is_scale(scale_detector.fisiko_minore_d_set, recognized_notes)
    assert result == is_fisiko_armoniko_scale