# sapphire-dg-client
Python client library to be used for fetching data from Sapphire Data Gateway!

## Installation

```shell
pip install git+https://github.com/hydrosolutions/sapphire-dg-client.git
```

## Usage

```python
from sapphire_dg import SapphireClient

client = SapphireClient(
    host="server host", # if not provided pointing to sapphire dg server
    api_key="api key" # api key for authorization to the sapphire dg server
)

# download forecast data for HRU 15149 for 2024-01-29, for all pf models
# provide directory to save the downloaded files - if not provider /tmp is used
client.ecmwf_ens.get_ensemble_forecast(
    hru_code="15149",
    date="2024-01-29",
    models=["pf"],
    directory="./tmp"
)
