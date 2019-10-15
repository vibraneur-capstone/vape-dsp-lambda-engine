import sys

import src.Algorithm as VapeAlgo
import src.DSPEngine as VapeDsp
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms


# f = open('./test/data.txt', "r")
# data = []
#
# if f.mode == "r":
#     file = f.readlines()
#
#     for line in file:
#         data.append(int(line))

DSP = VapeDsp.DSPEngine()

RMS = VapeAlgo.Algorithm(SupportedAlgorithms.RMS)
Kurtosis = VapeAlgo.Algorithm(SupportedAlgorithms.KURTOSIS)
FFT = VapeAlgo.Algorithm(SupportedAlgorithms.FFT)


# DSP.run(data)
