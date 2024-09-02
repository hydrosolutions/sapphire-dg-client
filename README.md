# sapphire-dg-client
Python client library to be used for fetching data from Sapphire Data Gateway!

## Installation

```shell
pip install git+https://github.com/hydrosolutions/sapphire-dg-client.git
export SAPPHIRE_DG_HOST="url-to-data-gateway" # You first have to put the url to the data gateway in the environment variable
```

## Usage

Download ECMWF ENS forecast data - example for HRU 15149 for 2024-01-29

```python
from sapphire_dg_client import SapphireDGClient

client = SapphireDGClient(
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
from sapphire_dg_client import SapphireDGClient

client = SapphireDGClient(
    api_key="wrong api key" # wrong api key for authorization to the sapphire dg server
)

# download some data
>>> files_downloaded = client.ecmwf_ens.get_ensemble_forecast(
    hru_code="15149",
    date="2024-01-29",
    models=["pf"],
     directory="./tmp"
)
...
File ~/.virtualenvs/sapphire-dg-gateway/lib/python3.11/site-packages/sapphire_dg_client/client_base.py:23, in SapphireDGClientBase._check_unauthorized(response)
     20 @staticmethod
     21 def _check_unauthorized(response: requests.Response):
     22     if response.status_code == 401:
---> 23         raise ValueError('Unauthorized. Please check your API key!')

ValueError: Unauthorized. Please check your API key!

```
Download ECMWF ENS raster forecast data - example for HRU 15149 for 2024-01-29

```python

client.ecmwf_ens.get_raster_forecast(parameter="2t", date="2024-02-22", models="all")
>>> ['/tmp/ecmwf-ens-param-2t-forcast-type-pf-60-80-35-45-coords.nc',
 '/tmp/ecmwf-ens-param-2t-forcast-type-cf-60-80-35-45-coords.nc']

```

Download operational data - example for HRU 15149 for 2023-01-01

```python
from sapphire_dg_client import SapphireDGClient

client = SapphireDGClient(
    api_key="api key" # api key for authorization to the sapphire dg server
)

resp = client.operational.get_control_spinup_and_forecast(
    hru_code="15149", 
    date="2023-01-01"
)
resp
>>> /tmp/Operational_HRU_15149_2023-01-01_2024-03-10.csv
```

Download ERA5 Land data - example for HRU 15149 for 2023-01-01

```python
from sapphire_dg_client import SapphireDGClient

client = SapphireDGClient(
    api_key="api key" # api key for authorization to the sapphire dg server
)
client.era5_land.get_era5_land("15149", date="2023-01-01", end_date="2023-01-31")
>>> '/tmp/HRU_15149_2023-01-01_2023-01-31.csv'
```

Download ERA5 Land raster files - example total_precipitation, 2m_temperature for 2024-08-24

```python
from sapphire_dg_client import SapphireDGClient

client = SapphireDGClient(
    api_key="api key" # api key for authorization to the sapphire dg server
)

client.era5_land.get_raster_reanalysis("total_precipitation", date="2024-08-24")
>>> ['/tmp/ecmwf-reanalysis-era5-land-param-total_precipitation.nc']

client.era5_land.get_raster_reanalysis("2m_temperature", date="2024-08-24")
>>> ['/tmp/ecmwf-reanalysis-era5-land-param-2m_temperature.nc']

```