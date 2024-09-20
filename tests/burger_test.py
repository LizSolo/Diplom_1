from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from conftest import burger, mock_bun, mock_ingredient

class TestBurger:

    def test_burger_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_burger_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient


    def test_burger_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1

    def test_burger_move_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_name.return_value = "Mocked Ingredient 2"
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient


    def test_burger_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        expected_price = (mock_bun.get_price() * 2) + (mock_ingredient.get_price() * 2)
        assert burger.get_price() == expected_price

    def test_burger_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        expected_receipt = (
            f"(==== Mocked Bun ====)\n"
            f"= filling Mocked Ingredient =\n"
            f"(==== Mocked Bun ====)\n\n"
            f"Price: {burger.get_price()}"
        )

        assert receipt == expected_receipt