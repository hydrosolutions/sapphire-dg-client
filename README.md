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
files_downloaded = client.ecmwf_ens.get_ensemble_forecast(
    hru_code="15149",
    date="2024-01-29",
    models=["pf"],
    directory="./tmp"
)
>>> files_downloaded
['./tmp/ECMWFIFS_20240129_ENS23_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS8_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS6_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS10_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS14_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS21_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS7_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS24_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS29_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS30_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS31_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS32_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS37_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS39_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS48_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS36_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS43_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS27_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS11_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS5_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS20_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS28_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS34_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS3_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS42_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS46_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS1_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS47_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS38_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS9_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS49_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS40_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS35_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS33_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS13_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS4_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS44_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS50_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS41_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS18_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS19_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS25_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS45_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS2_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS22_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS26_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS15_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS12_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS16_HRU15149.csv', './tmp/ECMWFIFS_20240129_ENS17_HRU15149.csv']

# downnload single model - use model number as string
files_downloaded = client.ecmwf_ens.get_ensemble_forecast(
    hru_code="15149",
    date="2024-01-29",
    models=["1"],
    directory="./tmp"
)

>>> files_downloaded
['./tmp/ECMWFIFS_20240129_ENS1_HRU15149.csv']

```

If wrong API_KEY is provided, the client will raise an exception.

```python
from sapphire_dg import SapphireClient
client = SapphireClient(
    host="server host", # if not provided pointing to sapphire dg server
    api_key="wrong api key" # wrong api key for authorization to the sapphire dg server
)

# download some data
>>> files_downloaded = client.ecmwf_ens.get_ensemble_forecast(
    hru_code="15149",
    date="2024-01-29",
    models=["pf"],
     directory="./tmp"
)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/some_path_to_system_installaton_here/sapphire-dg-gateway/lib/python3.11/site-packages/sapphire_dg_client/client.py", line 51, in get_ensemble_forecast
    raise ValueError(f"Failed to get ensemble forecast: {resp.text}")
ValueError: Failed to get ensemble forecast: {"detail": "Unauthorized"}


```


