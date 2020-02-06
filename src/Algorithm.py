import importlib

class Algorithm:
    def __init__(self, ID):
        self.ID = ID
        importlib.invalidate_caches()
        self.script = importlib.import_module(ID)

    def call(self, data):
        self.script.run(data)
