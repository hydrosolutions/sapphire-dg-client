import datetime

from .client_base import SapphireDGClientBase


class SapphireSnowModelClient(SapphireDGClientBase):
    SNOW_MODEL = "joel-snow-model"
    _parameters = ["HS", "SWE", "ROF", "HS24"]

    def _get_raster(
        self, parameter: str, date: str, forecast: bool = False, directory: str = "/tmp"
    ):
        if parameter not in self._parameters:
            raise ValueError(f"Invalid parameter. Must be one of {self._parameters}")

        endpoint = f"/api/raster/joel-snow-model/links?date={date}&parameter={parameter}&forecast={forecast}"
        return self._call_api_and_save_file(
            endpoint=endpoint,
            directory=directory,
        )

    def get_raster_reanalysis(
        self,
        parameter: str,
        date: str,
        directory: str = "/tmp",
    ):
        return self._get_raster(parameter, date, directory=directory)

    def get_raster_forecast(
        self,
        parameter: str,
        date: str,
        directory: str = "/tmp",
    ):
        # check if future date
        if datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d") < date:
            raise ValueError("Date must be in the past or today!")
        return self._get_raster(parameter, date, directory=directory, forecast=True)
