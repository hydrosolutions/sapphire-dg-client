import os
from typing import Union

import requests

from .client_base import SapphireDGClientBase


class SapphireECMWFENSClient(SapphireDGClientBase):
    _raster_parameters = {
        "2t",
        "tp",
    }

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

    @staticmethod
    def _directory_exists(directory: str):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _validate_ensemble_options(self, ensemble: str):
        if ensemble not in self._ensemble_options and ensemble not in self._pf_options:
            raise ValueError(
                f"Invalid ensemble option. Must be one of {self._ensemble_options} or for pf options 1 to 50"
            )

    def _add_model_to_endpoint(self, endpoint: str, models: list[str]):
        for model in models:
            endpoint = endpoint + f"&models={model}"
        return endpoint

    def _call_api_and_save_file(
            self,
            endpoint: str,
            directory: str
    ):
        resp = self._call_api(
            method="GET",
            endpoint=endpoint
        )

        files_downloaded = []
        self._directory_exists(directory)
        for file_resp in resp.json():
            resp = requests.get(file_resp.get('link'))
            local_file_path = self._save_file(resp, directory, file_resp['filename'])
            files_downloaded.append(local_file_path)
        return files_downloaded

    def get_ensemble_forecast(
            self,
            hru_code: str,
            date: str,
            models: list[str],
            directory: str = "/tmp"
    ):
        if isinstance(models, str):
            models = [models]

        for model in models:
            self._validate_ensemble_options(model)

        endpoint = f"api/calculations/ecmwf/template/RSMinerva/links?hru_code={hru_code}&date={date}&source=ENS"
        endpoint = self._add_model_to_endpoint(endpoint, models)
        return self._call_api_and_save_file(
            endpoint=endpoint,
            directory=directory,
        )


    def get_raster_forecast(
            self,
            parameter: str,
            date: str,
            models: Union[list[str], str],
            directory: str = "/tmp"
    ):
        if parameter not in self._raster_parameters:
            raise ValueError(f"Invalid parameter. Must be one of {self._raster_parameters}")

        if isinstance(models, str):
            models = [models]

        for model in models:
            self._validate_ensemble_options(model)

        endpoint = f"/api/raster/ecmwf-ens/links?date={date}&parameter={parameter}"
        endpoint = self._add_model_to_endpoint(endpoint, models)
        return self._call_api_and_save_file(
            endpoint=endpoint,
            directory=directory,
        )
