import scale_detector
import numpy as np
import pytest


    # Define the test cases using the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("recognized_notes, is_fisiko_armoniko_scale", [
    (np.array(["E0","F0","G0"]), True),
    # Add more test cases here as needed
])
def test_detect_scale(recognized_notes, is_fisiko_armoniko_scale):
    result = scale_detector.detect_scale(recognized_notes)
    assert result == is_fisiko_armoniko_scale