from BreadCalc import calc_sourdough_bread, recipes
from BreadCalc.plans import SourdoughBreadPlan
from BreadCalc.recipes import SourdoughBreadRecipe


def test_plan_returns_recipe():
    plan = SourdoughBreadPlan(
        hydration=1,
        total_flour=100,
        sourdough=100,
        sourdough_hydration=1,
        salt=0.02,
    )
    recipe = calc_sourdough_bread(plan)
    assert isinstance(recipe, SourdoughBreadRecipe)


def test_my_default_recipes_plan_returns_has_222g_water_and_350g_flour():
    plan = _get_default_recipe()
    recipe = calc_sourdough_bread(plan)
    assert recipe.flour_rest == 350
    assert recipe.water_rest == 222
    assert recipe.salt == 8


def test_my_default_recipe_hast_sour_percentage_of_13():
    plan = _get_default_recipe()
    recipe = calc_sourdough_bread(plan)
    assert recipe.sour_ratio == 0.125


def _get_default_recipe() -> SourdoughBreadPlan:
    return SourdoughBreadPlan(
        hydration=0.63,
        total_flour=400,
        sourdough=80,
        sourdough_hydration=0.6,
        salt=0.02,
    )
