from .client_base import SapphireDGClientBase


class SapphireEra5LandClient(SapphireDGClientBase):
    _raster_parameters = {
        "2m_temperature",
        "total_precipitation",
    }

    def get_era5_land(
        self, hru_code: str, date: str, end_date: str = None, directory: str = "/tmp"
    ):
        endpoint = (
            "api/calculations/era5-land/template/RSMinerva"
            f"?hru_code={hru_code}&start_date={date}"
        )
        if end_date:
            endpoint = endpoint + f"&end_date={end_date}"

        resp = self._call_api(method="GET", endpoint=endpoint)

        cd = resp.headers.get("Content-Disposition")
        if cd and "filename" in cd:
            filename = cd.split("filename=")[1]
        else:
            filename = f"era5_land_{hru_code}_{date}.csv"

        return self._save_file(resp, directory, filename)

    def get_raster_reanalysis(
        self,
        parameter: str,
        date: str,
        directory: str = "/tmp",
    ):
        if parameter not in self._raster_parameters:
            raise ValueError(
                f"Invalid parameter. Must be one of {self._raster_parameters}"
            )

        endpoint = f"/api/raster/era5-land/links?day={date}&parameter={parameter}"
        return self._call_api_and_save_file(
            endpoint=endpoint,
            directory=directory,
        )
