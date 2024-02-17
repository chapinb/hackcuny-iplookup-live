from typing import Self
from unittest import TestCase

from app.ip_utils import get_ip_address_location, is_ip_address


class TestIpUtils(TestCase):
    def test_is_ip_address(self: Self) -> None:
        # Assembly
        sample_value = "1.1.1.1"
        # Action
        is_ip = is_ip_address(sample_value)
        # Assertion
        self.assertTrue(is_ip)

    def test_get_ip_address_location(self: Self) -> None:
        # Assembly
        sample_ip_address = "2.2.2.2"
        # Action
        actual_location = get_ip_address_location(sample_ip_address)
        expected_location = {
            "lat": 48.8566,
            "lon": 2.35222,
            "city": "Paris",
            "country": "France",
        }
        self.assertEqual(expected_location, actual_location)
