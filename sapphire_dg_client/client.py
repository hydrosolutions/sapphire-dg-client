from .ecmwf import SapphireECMWFENSClient
from .era5_land import SapphireEra5LandClient
from .operational import SapphireOperationalClient


class SapphireDGClient:

    def __init__(self, api_key, host="https://data-gateway.ieasyhydro.org/"):
        self.host = host
        self.api_key = api_key
        self.ecmwf_ens = SapphireECMWFENSClient(host, api_key)
        self.operational = SapphireOperationalClient(host, api_key)
        self.era5_land = SapphireEra5LandClient(host, api_key)
