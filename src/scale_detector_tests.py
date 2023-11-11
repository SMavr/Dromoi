import scale_detector
import numpy as np
import pytest


@pytest.mark.parametrize("recognized_notes, is_fisiko_armoniko_scale", [
    (np.array(["E0","F0","G0"]), True),
    (np.array(["E0", "F#0", "G0"]), False)
])
def test_detect_scale(recognized_notes, is_fisiko_armoniko_scale):
    result = scale_detector.detect_scale(recognized_notes)
    assert result == is_fisiko_armoniko_scale