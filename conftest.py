import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = "Mocked Bun"
    mock_bun.get_price.return_value = 150
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_name.return_value = "Mocked Ingredient"
    mock_ingredient.get_price.return_value = 250
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_ingredient