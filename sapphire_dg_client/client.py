import os

import requests

from .client_base import SapphireDGClientBase


class SapphireECMWFENSClient(SapphireDGClientBase):

    _ensemble_options = {
        "all",
        "cf",
        "pf",
    }

    # pf options 1 to 50 string
    _pf_options = set(map(str, range(1, 51)))

    def __init__(
            self,
            host=None,
            api_key=None,
    ):
        super().__init__(host, api_key)

    def _directory_exists(self, directory: str):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _validate_ensemble_options(self, ensemble: str):
        if ensemble not in self._ensemble_options and ensemble not in self._pf_options:
            raise ValueError(
                f"Invalid ensemble option. Must be one of {self._ensemble_options} or for pf options 1 to 50"
            )

    def get_ensemble_forecast(
            self,
            hru_code: str,
            date: str,
            models: list[str],
            directory: str = "/tmp"
    ):
        endpoint = f"api/calculations/ecmwf/template/RSMinerva/links?hru_code={hru_code}&date={date}&source=ENS"
        for m in models:
            endpoint = endpoint + f"&models={m}"
        resp = self._call_api(
            method="GET",
            endpoint=endpoint
        )
        if resp.status_code != 200:
            raise ValueError(f"Failed to get ensemble forecast: {resp.text}")
        files_downloaded = []
        self._directory_exists(directory)
        for file_resp in resp.json():
            local_file_path = f"{directory}/{file_resp['filename']}"
            with open(local_file_path, "wb") as f:
                write = requests.get(file_resp.get('link')).content
                f.write(write)
                files_downloaded.append(local_file_path)
        return files_downloaded


class SapphireDGClient:

    def __init__(self, host, api_key):
        self.host = host
        self.api_key = api_key
        self.ecmwf_ens = SapphireECMWFENSClient(host, api_key)
