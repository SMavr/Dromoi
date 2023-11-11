import unittest
import scale_detector
import numpy as np

class TestScaleDetect(unittest.TestCase):
  
    def test_detect_scale(self):
        recognized_notes = np.array(["F3", "C3"]);
        result = scale_detector.detect_scale(recognized_notes)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()