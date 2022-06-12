from pywebio import start_server
from pywebio.input import FLOAT, NUMBER, input, input_group
from pywebio.output import put_text

from BreadCalc.plans import SourdoughBreadPlan
from BreadCalc.recipes import SourdoughBreadRecipe


def calc_sourdough_bread(plan: SourdoughBreadPlan) -> SourdoughBreadRecipe:
    _sour_flour = plan.sourdough / (1 + plan.sourdough_hydration)
    _sour_water = plan.sourdough - _sour_flour
    _flour_rest = plan.total_flour - _sour_flour
    _total_water = plan.total_flour * plan.hydration
    _water_rest = _total_water - _sour_water
    _salt = plan.total_flour * plan.salt
    return SourdoughBreadRecipe(
        plan=plan, flour_rest=_flour_rest, water_rest=_water_rest, salt=_salt
    )


def show_pywebio():
    data = input_group(
        "Your Bread Plan",
        [
            input(
                "Total Flour Amount in g",
                name="total_flour",
                type=NUMBER,
                other_html_attrs={"step": 50},
            ),
            input(
                "Hydration as decimal",
                name="hydration",
                type=FLOAT,
                placeholder=".99 for a hydration of 99%",
            ),
            input("Amount of Sourdough in g", name="sourdough", type=NUMBER),
            input(
                "Sourdough's Hydration",
                name="sourdough_hydration",
                type=FLOAT,
                placeholder="1.05 for a hydration of 105%",
            ),
            input("Salt", name="salt", type=FLOAT, placeholder="0.05 for 5%"),
        ],
    )
    plan = SourdoughBreadPlan(
        total_flour=data["total_flour"],
        hydration=data["hydration"],
        sourdough=data["sourdough"],
        sourdough_hydration=data["sourdough_hydration"],
        salt=data["salt"],
    )
    recipe: SourdoughBreadRecipe = calc_sourdough_bread(plan)
    put_text(f"Remaining flour: {recipe.flour_rest}g")
    put_text(f"Remaining water: {recipe.water_rest}g")
    put_text(f"Salt: {recipe.salt}g")
    put_text(f"This bread will have {recipe.sour_ratio * 100}% of sour flour.")


if __name__ == "__main__":
    start_server(show_pywebio, port=8000, debug=True)
