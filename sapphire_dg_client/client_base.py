import os
from urllib.parse import urljoin

import requests


class SapphireDGClientBase:
    def __init__(
        self,
        host=None,
        api_key=None,
    ):
        self.host = host or os.environ.get("SAPPHIRE_DG_HOST")
        self.api_key = api_key or os.environ.get("SAPPHIRE_DG_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required for client library to work!")
        if not self.host:
            raise ValueError("Host is required for client library to work!")

    @staticmethod
    def _check_unauthorized(response: requests.Response):
        if response.status_code == 401:
            raise ValueError("Unauthorized. Please check your API key!")

    @staticmethod
    def _save_file(response: requests.Response, directory: str, filename: str):
        file = f"{directory}/{filename}"
        with open(file, "wb") as f:
            f.write(response.content)
        return file

    @staticmethod
    def _directory_exists(directory: str):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _call_api_and_save_file(self, endpoint: str, directory: str):
        resp = self._call_api(method="GET", endpoint=endpoint)

        files_downloaded = []
        self._directory_exists(directory)
        for file_resp in resp.json():
            resp = requests.get(file_resp.get("link"))
            local_file_path = self._save_file(resp, directory, file_resp["filename"])
            files_downloaded.append(local_file_path)
        return files_downloaded

    def _call_api(
        self,
        method: str,
        endpoint: str,
        headers: dict = None,
        body: dict = None,
    ) -> requests.Response:
        endpoint = endpoint + f"&api_key={self.api_key}"
        response = requests.request(
            method, urljoin(self.host, endpoint), headers=headers, data=body
        )
        if response.status_code != 200:
            raise ValueError(f"Failed to get data from {endpoint}: {response.text}")

        self._check_unauthorized(response)
        return response
