import unittest
import os
import src.algorithms.kurtosis.Kurtosis as kurto
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms as enums


class MyTestCase(unittest.TestCase):
    f = open(os.path.dirname(__file__)+'/data.txt', "r")
    testData = []

    def test_kurtosis_computation(self):
        for line in self.f.readlines():
            self.testData.append(int(line))

        result = kurto.run(self.testData)
        assert round(18.0451347234, 10) == round(result.result, 10)
        assert enums.KURTOSIS == result.resultType
        assert result.timestamp is not None