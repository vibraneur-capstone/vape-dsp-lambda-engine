import numpy as np
from src.dto.resultEncapsulation import ResultEncapsulation
from src.algorithms.AlgorithmsEnums import SupportedAlgorithms


def lambda_entry(event, context):
    if 'data' not in event:
        return {
            'statusCode': 400,
            'description': 'missing data'
        }
    result = run(event['data'])

    return {
        'statusCode': 200,
        'body': result.toJsonString()
    }


def run(data):
    # TODO:::: this computes a double sided spectrum. We may wanna compute only for single sided
    fft = np.fft.fft(data)
    # encapsulate result into ResultEncapsulation object for easier integration
    return ResultEncapsulation(result=fft, inputData=data, resultType=SupportedAlgorithms.FFT)
