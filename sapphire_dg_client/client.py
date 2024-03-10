from .ecmwf import SapphireECMWFENSClient
from .operational import SapphireOperationalClient


class SapphireDGClient:

    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key
        self.ecmwf_ens = SapphireECMWFENSClient(host, api_key)
        self.operational = SapphireOperationalClient(host, api_key)
