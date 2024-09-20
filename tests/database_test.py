from database import Database
from ..praktikum.bun import Bun
from ..praktikum.ingredient import Ingredient
from ..praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

expected_buns = [
    Bun("black bun", 100),
    Bun("white bun", 200),
    Bun("red bun", 300)
]

expected_ingredients = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
]

class TestDataBase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == len(expected_buns)

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == len(expected_ingredients)