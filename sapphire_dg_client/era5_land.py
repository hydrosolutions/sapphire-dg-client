from .client_base import SapphireDGClientBase


class SapphireEra5LandClient(SapphireDGClientBase):

    def get_era5_land(
            self,
            hru_code: str,
            date: str,
            end_date: str = None,
            directory: str = "/tmp"

    ):
        endpoint = f"api/calculations/era5-land/template/RSMinerva?hru_code={hru_code}&start_date={date}"
        if end_date:
            endpoint = endpoint + f"&end_date={end_date}"

        resp = self._call_api(
            method="GET",
            endpoint=endpoint
        )

        cd = resp.headers.get('Content-Disposition')
        if cd and "filename" in cd:
            filename = cd.split("filename=")[1]
        else:
            filename = f"era5_land_{hru_code}_{date}.csv"

        return self._save_file(resp, directory, filename)
