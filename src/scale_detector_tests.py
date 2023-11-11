import scale_detector
import numpy as np
import pytest

@pytest.mark.parametrize("recognized_notes",[
    np.array(["E0","F0","G0"])
])
  
def test_detect_scale(recognized_notes):
    result = scale_detector.detect_scale(recognized_notes)
    assert result == True