import math
import src.dto.resultEncapsulation as Vape
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms


def run(data):

    # Define variables
    sumOfSquares = 0

    # Summation for the sum of sqaures
    for d in data:
        sumOfSquares += d*d

    # Calculate RMS through the square root of the average of the sum of squares
    rms = math.sqrt(sumOfSquares/len(data))

    return Vape.ResultEncapsulation(result=rms, resultType=SupportedAlgorithms.RMS)