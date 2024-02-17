import ipaddress

import requests


def is_ip_address(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def get_ip_address_location(value: str) -> dict[str, str | float]:
    response = requests.get(
        f"http://ip-api.com/json/{value}",
        timeout=30,
    )
    response.raise_for_status()
    response_data = response.json()

    fields_we_care_about = ["lat", "lon", "city", "country"]

    return {x: response_data[x] for x in fields_we_care_about}
