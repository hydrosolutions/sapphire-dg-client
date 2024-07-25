import os

from .ecmwf import SapphireECMWFENSClient
from .era5_land import SapphireEra5LandClient
from .operational import SapphireOperationalClient


class SapphireDGClient:

    def __init__(self, api_key, host=None):
        self.host = host or os.environ.get('SAPPHIRE_DG_HOST')
        self.api_key = api_key
        self.ecmwf_ens = SapphireECMWFENSClient(host, api_key)
        self.operational = SapphireOperationalClient(host, api_key)
        self.era5_land = SapphireEra5LandClient(host, api_key)
