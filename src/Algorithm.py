import importlib

class Algorithm:
    def __init__(self, ID):
        self.ID = ID.value
        importlib.invalidate_caches()
        print('Initializing script:' + 'src.algorithm.' + ID.value.lower() + '.' + ID.value)
        try:
            self.script = importlib.import_module(str('src.algorithms.' + ID.value.lower() + '.' + ID.value))
        except ImportError as err:
            print('Error:', err)


    def call(self, data):
        self.script.run(data)
