import sys

sys.path.insert(0, 'src/algorithms/..')

import src.Algorithm as VapeAlgo
import src.DSPEngine as VapeDsp
from src.algorithms.AlgorithmsEnums import AlgorithmID

# f = open('./test/data.txt', "r")
# data = []
#
# if f.mode == "r":
#     file = f.readlines()
#
#     for line in file:
#         data.append(int(line))

DSP = VapeDsp.DSPEngine()

RMS = VapeAlgo.Algorithm(AlgorithmID.RMS.name)
Kurtosis = VapeAlgo.Algorithm(AlgorithmID.KURTOSIS.name)
FFT = VapeAlgo.Algorithm(AlgorithmID.FFT.name)

# DSP.run(data)
