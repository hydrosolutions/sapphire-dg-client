from .client_base import SapphireDGClientBase


class SapphireOperationalClient(SapphireDGClientBase):

    def get_control_spinup_and_forecast(
            self,
            hru_code: str,
            date: str,
            directory: str = "/tmp",
    ):
        endpoint = f"api/calculations/operational/template/?hru_code={hru_code}&start_date={date}"
        resp = self._call_api(
            method="GET",
            endpoint=endpoint
        )
        if resp.status_code != 200:
            raise ValueError(f"Failed to get control spinup and forecast: {resp.text}")
        cd = resp.headers.get('Content-Disposition')
        if cd and "filename" in cd:
            filename = cd.split("filename=")[1]
        else:
            filename = f"control_spinup_and_forecast_{hru_code}_{date}.csv"

        return self._save_file(resp, directory, filename)
