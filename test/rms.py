import os
import src.algorithms.rms.RMS as rms
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms as enums


class RmsTest:
    data = open(os.path.dirname(__file__)+'/data.txt', "r")
    testData = []

    def test_rms_computation(self):
        for line in self.data.readlines():
            self.testData.append(int(line))

        result = rms.run(self.testData)
        assert round(47.7132211299, 10) == round(result.result, 10)
        assert enums.RMS == result.resultType
        assert result.timestamp is not None

