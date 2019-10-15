import numpy as np
import src.dto.resultEncapsulation as Vape
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms

def run(data):
    # TODO:::: this computes a double sided spectrum. We may wanna compute only for single sided
    fft = np.fft.fft(data)
    # encapsulate result into ResultEncapsulation object for easier integration
    return Vape.ResultEncapsulation(result=fft, resultType=SupportedAlgorithms.FFT)
