class DSPEngine:

    def __init__(self):
        print('Initializing DSP Engine...')
        self.algorithms = []

    '''
    TODO::: we need to think how we structure this run() function. The current structure precludes the possibility of
    running multiple algorithms in parallel. Also, it's harder to integrate with data pipeline
    '''
    def run(self, data):
        print("Running DSP Engine...")
        for a in self.algorithms:
            a.call(data)

    def add(self, algorithm):
        print("Adding script: " + algorithm.ID)
        self.algorithms.append(algorithm)

    def remove(self, algorithm):
        self.algorithms.remove(algorithm)
