import environment.dev
import environment.uat
import environment.prod


class VapeEnvironment:
    environment = {
        'dev': dev.DevEnvironment,
        'uat': uat.UatEnvironment,
        'prod': prod.ProdEnvironment
    }

    def __init__(self):
        # toggle configuration in other environment
        self.current = self.environment.get('dev')
