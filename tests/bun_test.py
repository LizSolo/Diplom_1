import pytest

from ..praktikum.bun import Bun


@pytest.mark.parametrize('bun_name, bun_price', [
    ("white bun", 200),
    ("black bun", 100),
    ("red bun", 300)
])
class TestBun:

    def test_bun_get_name(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    def test_bun_get_price(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price