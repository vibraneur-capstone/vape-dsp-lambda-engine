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

    # Calculates the fft.
    fft = parse_complex_number(np.fft.fft(data))

    # TODO:::: use the FFT to compute the SFB using the method outlined in the research paper

    # Splits the fft into the single sided spectrum
    single_fft = fft[len(fft)//2:]

    # encapsulate result into ResultEncapsulation object for easier integration
    return ResultEncapsulation(result=fft, inputData=data, resultType=SupportedAlgorithms.SFB)


def parse_complex_number(complex_arr):
    parsed = []
    for num in complex_arr:
        complex_str = str(num).strip().replace("(", '', 1).replace(")", '', 1)
        parsed.append(complex_str)
    return parsed
