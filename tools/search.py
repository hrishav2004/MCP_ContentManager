import requests
from typing import Optional, Dict, Any


BASE_URL = "http://localhost/CMServiceAPI/Record"


def search_records(
    record_number: Optional[str] = None,
    status: Optional[str] = None,
    created_date: Optional[str] = None,
    properties: str = "NameString",
    response_format: str = "json",
) -> Dict[str, Any]:
    """
    Call CMServiceAPI Record search with structured parameters.
    """

    params = {
        "format": response_format,
        "Properties": properties,
    }

    query_parts = []

    if record_number:
        query_parts.append(f"number:{record_number}")

    if status:
        query_parts.append(f"status:{status}")

    if created_date:
        query_parts.append(f"created:{created_date}")

    if query_parts:
        params["q"] = "/".join(query_parts)

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10,
    )

    response.raise_for_status()
    return response.json()
