import importlib

class Algorithm:
    def __init__(self, ID):
        self.ID = ID.value
        importlib.invalidate_caches()
        print('Initializing script: ' + self.ID)
        try:
            self.script = importlib.import_module(str('src.algorithms.' + ID.value.lower() + '.' + ID.value))
        except ImportError as err:
            print('Error:', err)


    def call(self, data):
        print("Running script: " + self.ID)
        self.script.run(data)
