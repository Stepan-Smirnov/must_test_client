import datetime as dt
from datetime import datetime
from typing import Any

import requests

from app.constants import API_URL, TIMEOUT_REQUEST
from app.exception import BadAPIResponse


class DataAPI:
    """class for data API methods"""

    @staticmethod
    def get_data(
        page: int = 1,
        per_page: int = 10,
    ) -> dict[str, Any]:
        """GET data list"""

        params = dict(page=page, per_page=per_page)
        response = requests.get(
            url=API_URL, params=params, timeout=TIMEOUT_REQUEST
        )
        r_json: dict = response.json()
        if response.status_code != requests.codes.ok:
            raise BadAPIResponse(f"API error {response.json()}")
        return r_json

    @staticmethod
    def add_data(
        text: str,
        sequence_number: int,
    ) -> None:
        """add data item"""

        json = dict(
            text=text,
            sequence_number=sequence_number,
            created_at=str(datetime.now(tz=dt.UTC)),
        )

        response = requests.post(
            url=API_URL, json=json, timeout=TIMEOUT_REQUEST
        )
        if response.status_code != requests.codes.ok:
            raise BadAPIResponse(f"API error {response.json()}")
