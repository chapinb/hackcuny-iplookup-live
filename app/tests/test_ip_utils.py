from typing import Self
from unittest import TestCase

from app.ip_utils import is_ip_address


class TestIpUtils(TestCase):
    def test_is_ip_address(self: Self) -> None:
        # Assembly
        sample_value = "1.1.1.1"
        # Action
        is_ip = is_ip_address(sample_value)
        # Assertion
        self.assertTrue(is_ip)
